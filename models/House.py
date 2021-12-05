from models.Property import Property


class House(Property):
    def __init__(self, area: str, rooms: int, price: int, address: str, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"Nieruchomość w rejonie '{self.area}', przy ulicy '{self.address}', cena {self.price}, " + \
               f"liczba pokoi {self.rooms}, rozmiar: '{self.plot}'"