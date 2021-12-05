from models.Student import Student


student1 = Student("Andrzej", 75)
student2 = Student("Paweł", 40)

print(student1.is_passed())
print(student2.is_passed())
