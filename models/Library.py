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