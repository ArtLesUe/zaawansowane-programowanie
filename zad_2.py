from models.Student import Student
from models.Library import Library
from models.Book import Book
from models.Employee import Employee
from models.Order import Order


library_a = Library("Rybnik", "ul. Wawelska 12", "44-217", "08:00-16:00", "000-000-000")
library_b = Library("Katowice", "ul. Różana 55", "55-555", "08:00-16:00", "111-111-111")

book_a = Book(library_a, "2021-01-01", "Andrzej", "Zmyślony", 100)
book_b = Book(library_a, "2021-01-02", "Paweł", "Zmyślony", 300)
book_c = Book(library_b, "2021-01-03", "Maciej", "Zmyślony", 200)
book_d = Book(library_b, "2021-01-04", "Grzegorz", "Zmyślony", 250)
book_e = Book(library_b, "2021-01-05", "Marek", "Zmyślony", 50)

employee_a = Employee("Paweł", "Niemataki", "2021-11-11", "1980-01-01", "Warszawa", "ul. Wawelska 11", "00-000", "1234")
employee_b = Employee("Andrzej", "Niemataki", "2021-11-11", "1980-01-01", "Warszawa", "ul. Polna 11", "00-000", "1234")
employee_c = Employee("Jan", "Niemataki", "2021-11-11", "1980-01-01", "Warszawa", "ul. Wawelska 11", "00-000", "1234")

student_a = Student("Jan Nowak", 100)
student_b = Student("Paweł Niemamnie", 80)
student_c = Student("Ireneusz Krosny", 49)

order_a = Order(employee_a, student_a, book_a, "2021-11-11")
order_b = Order(employee_b, student_b, book_c, "2021-12-12")

print(order_a)
print(order_b)
