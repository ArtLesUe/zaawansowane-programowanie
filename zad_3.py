class Property:
    def __init__(self, area: str, rooms: int, price: int, address: str):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Nieruchomość w rejonie '{self.area}', przy ulicy '{self.address}', cena {self.price}, " + \
               f"liczba pokoi {self.rooms}"


class House(Property):
    def __init__(self, area: str, rooms: int, price: int, address: str, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"Nieruchomość w rejonie '{self.area}', przy ulicy '{self.address}', cena {self.price}, " + \
               f"liczba pokoi {self.rooms}, rozmiar: '{self.plot}'"


class Flat(House):
    def __init__(self, area: str, rooms: int, price: int, address: str, plot: int, floor: int):
        super().__init__(area, rooms, price, address, plot)
        self.floor = floor

    def __str__(self):
        return f"Nieruchomość w rejonie '{self.area}', przy ulicy '{self.address}', cena {self.price}, " + \
               f"liczba pokoi {self.rooms}, rozmiar: '{self.plot}', piętro: '{self.floor}'"


house_a = House("Zamojście", 5, 220000, "ul. Gliwicka 12", 95)
flat_a = Flat("Ursynów", 3, 300000, "ul. Poznańska 11", 55, 2)

print(house_a)
print(flat_a)
