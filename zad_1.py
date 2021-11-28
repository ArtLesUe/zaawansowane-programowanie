class Student:
    def __init__(self, name: str, marks: int):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        return self.marks > 50


student1 = Student("Andrzej", 75)
student2 = Student("Paweł", 40)

print(student1.is_passed())
print(student2.is_passed())
