import sys
import bisect
import uuid
from request import Request
from user import User


class Assignement:
    def __init__(self, path, remaining_requests, remaining_users) -> None:
        self.path = path
        self.remaining_requests = remaining_requests
        self.remaining_users = remaining_users
        self.score = 0
        self.uid = str(uuid.uuid1()).split("-")[0]

    def __lt__(self, other):
        return self.score < other.score

    def __str__(self) -> str:
        path_str = ", ".join(f"({request},{user},{score})" for (
            request, user, score) in self.path)
        return f"Assignement<uid:{self.uid}, score:{self.score}, path:({path_str})>"


class Resolver:
    def __init__(self, users, requests, compute_score_func) -> None:
        self._request_number = len(requests)
        self._assignements = [Assignement(
            [], requests.copy(), users.copy())]
        self._score_computation_numbers = 0
        self._compute_score_func = compute_score_func
        self._verbose = False
        self._computed_score_mapping = {}

    def set_verbose(self, activate_verbose):
        self._verbose = activate_verbose

    def _compute_next_step(self, assignement: Assignement):
        if self._verbose:
            print(assignement.uid, assignement.remaining_users,
                  assignement.remaining_requests)
        new_assignements = []
        new_remaining_requests = assignement.remaining_requests.copy()
        current_request: Request = new_remaining_requests.pop(0)
        for user_idx in range(0, len(assignement.remaining_users)):
            new_remaining_users = assignement.remaining_users.copy()
            current_user: User = new_remaining_users.pop(user_idx)

            key = f"{current_user}-{current_request}"
            if key in self._computed_score_mapping:
                score = self._computed_score_mapping[key]
            else:
                score = self._compute_score_func(current_user, current_request)
                self._computed_score_mapping[key] = score
                self._score_computation_numbers += 1

            path = assignement.path + [(current_request, current_user, score)]
            new_assignement = Assignement(
                path, new_remaining_requests, new_remaining_users)
            new_assignement.score = assignement.score + score
            new_assignements.append(new_assignement)
        return new_assignements

    def resolve(self) -> Assignement:
        assignement = self._assignements.pop(0)
        while len(assignement.remaining_requests):
            for new_assignement in self._compute_next_step(assignement):
                bisect.insort(self._assignements, new_assignement)
            if self._verbose:
                for ass in self._assignements:
                    print(ass)
                print("+++++++")
            assignement = self._assignements.pop(0)

        return assignement, self._score_computation_numbers
