from models.House import House


class Flat(House):
    def __init__(self, area: str, rooms: int, price: int, address: str, plot: int, floor: int):
        super().__init__(area, rooms, price, address, plot)
        self.floor = floor

    def __str__(self):
        return f"Nieruchomość w rejonie '{self.area}', przy ulicy '{self.address}', cena {self.price}, " + \
               f"liczba pokoi {self.rooms}, rozmiar: '{self.plot}', piętro: '{self.floor}'"