class Property:
    def __init__(self, area: str, rooms: int, price: int, address: str):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Nieruchomość w rejonie '{self.area}', przy ulicy '{self.address}', cena {self.price}, " + \
               f"liczba pokoi {self.rooms}"