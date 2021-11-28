class Student:
    def __init__(self, name: str, marks: int):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Student {self.name}, ocena {self.marks}"

    def is_passed(self) -> bool:
        return self.marks > 50


class Library:
    def __init__(self, city: str, street: str, zip_code: str, open_hours: str, phone: int):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Biblioteka pod adresem {self.street}, {self.zip_code}, {self.city}," + \
               f"godziny otwarcie {self.open_hours}, telefon {self.phone}"


class Book:
    def __init__(self, library: Library, publication_date: str, author_name: str,
                 author_surname: str, number_of_pages: int):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Książka autorstwa {self.author_name} {self.author_surname}, opublikowana {self.publication_date}, " + \
               f"liczba stron {self.number_of_pages}, w lokacji: {self.library}"


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

    def __str__(self):
        return f"Pracownik {self.first_name} {self.last_name}, zatrudniony {self.hire_date}, urodzony: " + \
               f"{self.birth_date}, adres: {self.street}, {self.zip_code} {self.city}, telefon: {self.phone}"


class Order:
    def __init__(self, employee: Employee, student: Student, books: Book, order_date: str):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f"Zamówienie studenta '{self.student}', z dnia {self.order_date}, na książkę '{self.books}', " + \
               f"obsługujący zamówienie '{self.employee}'"


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
