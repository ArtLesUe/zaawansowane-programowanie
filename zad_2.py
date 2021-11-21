class Library:
    def __init__(self, city: str, street: str, zip_code: str, open_hours: str, phone: int):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone


class Book:
    def __init__(self, library: Library, publication_date: str, author_name: str,
                 author_surname: str, number_of_pages: str):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages


class Employee:
    def __init__(self, first_name: str, last_name: str, hire_date: str, birth_date: str,
                 city: str, street: str, zip_code: str, phone: str):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone


class Order:
    def __init__(self, employee: Employee, student: str, books: Book, order_date: str):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date
