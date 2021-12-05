from models.Employee import Employee
from models.Student import Student
from models.Book import Book


class Order:
    def __init__(self, employee: Employee, student: Student, books: Book, order_date: str):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f"Zamówienie studenta '{self.student}', z dnia {self.order_date}, na książkę '{self.books}', " + \
               f"obsługujący zamówienie '{self.employee}'"