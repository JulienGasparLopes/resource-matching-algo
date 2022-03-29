class User:
    def __init__(self, uid, criterion_1, criterion_2) -> None:
        self.uid = uid
        self.criterion_1 = criterion_1
        self.criterion_2 = criterion_2

    def __str__(self) -> str:
        return f"User<{self.uid}>"
