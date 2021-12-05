from datetime import datetime

from models.FirmaTransportowa import FirmaTransportowa


class Pojazd:
    def __init__(self, plate_number: str, max_cargo_kg: int, max_cargo_m3: int, buy_in_year: int,
                 next_service_check: datetime, car_mark: str, owner_company: FirmaTransportowa) -> None:
        self._plate_number = plate_number
        self._max_cargo_kg = max_cargo_kg
        self._max_cargo_m3 = max_cargo_m3
        self._buy_in_year = buy_in_year
        self._next_service_check = next_service_check
        self._owner_company = owner_company
        self._car_mark = car_mark

    def __str__(self) -> str:
        return f"Pojazd o numerze rejestracyjnym {self._plate_number}, marki {self._car_mark}, maksymalny udźwig: " + \
            f"{self._max_cargo_kg} kg, objętość paki: {self._max_cargo_m3}, rocznik {self._buy_in_year}, " + \
            f"następny przegląd {self._next_service_check}, należy do firmy: '{self._owner_company}'."

    @property
    def car_mark(self) -> str:
        return self._car_mark