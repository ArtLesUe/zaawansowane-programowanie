class Student:
    def __init__(self, name: str, marks: int):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Student {self.name}, ocena {self.marks}"

    def is_passed(self) -> bool:
        return self.marks > 50