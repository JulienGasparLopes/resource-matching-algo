from random import randint
from request import Request
from resolver import Resolver
from user import User


def case_perfect_fit():
    users = [
        User("1", "A", "one"),
        User("2", "B", "two"),
    ]
    requests = [
        Request("1", ["A"], ["one"]),
        Request("2", ["B"], ["two"]),
    ]
    return users, requests


def case_one_fit():
    users = [
        User("1", "A", "one"),
        User("2", "B", "two"),
    ]
    requests = [
        Request("1", ["A"], ["two"]),
        Request("2", ["A", "B"], ["one"]),
    ]
    return users, requests


def case_hundred():
    crit_1_values = ["A", "B", "C", "D"]
    crit_2_values = ["one", "two", "three", "four"]
    users = []
    requests = []
    for i in range(0, 12):
        users.append(
            User(i, crit_1_values[randint(0, 3)], crit_2_values[randint(0, 3)]))
        crit_1 = set([crit_1_values[randint(0, 3)] for _ in range(0, 3)])
        crit_2 = set([crit_2_values[randint(0, 3)] for _ in range(0, 3)])
        requests.append(Request(i, crit_1, crit_2))
    return users, requests


def compute_score(resource, request):
    score_criterion_1 = 0 if request.has_criterion_1(
        resource.criterion_1) else 2
    score_criterion_2 = 0 if request.has_criterion_2(
        resource.criterion_2) else 2
    return score_criterion_1 + score_criterion_2


if __name__ == "__main__":
    # requests, resources = case_perfect_fit()
    # users, requests = case_one_fit()
    users, requests = case_hundred()

    print()
    print("===== Input Users =====")
    for user in users:
        print(user, user.criterion_1, user.criterion_2)
    print("===== Input Requests =====")
    for request in requests:
        print(request, request.criterion_1, request.criterion_2)

    print()
    print("===== Resolve =====")
    resolver = Resolver(users, requests, compute_score)
    # resolver.set_verbose(True)
    max_assignement, score_computation_number = resolver.resolve()

    print(
        f"Best answer with score {max_assignement.score} is {max_assignement}")
    print(f"Done {score_computation_number} score computations")
