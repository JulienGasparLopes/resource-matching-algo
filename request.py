class Request:
    def __init__(self, uid, criterion_1_list, criterion_2_list) -> None:
        self.uid = uid
        self.criterion_1 = criterion_1_list
        self.criterion_2 = criterion_2_list

    def has_criterion_1(self, criterion):
        return criterion in self.criterion_1

    def has_criterion_2(self, criterion):
        return criterion in self.criterion_2

    def __str__(self) -> str:
        return f"Request<{self.uid}>"
