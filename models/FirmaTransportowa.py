from models.Firma import Firma


class FirmaTransportowa(Firma):
    def __init__(self, company_name: str, owner_name: str, year_of_start: int, address_street: str,
                 address_postal: str, address_city: str, company_value_in_mil: int, number_of_cars: int,
                 max_delivery_range_in_km: int, workers: int, workers_on_free_day: int) -> None:
        super().__init__(company_name, owner_name, year_of_start, address_street, address_postal, address_city)
        self._company_value_in_mil = company_value_in_mil
        self._number_of_cars = number_of_cars
        self._max_delivery_range_in_km = max_delivery_range_in_km
        self._workers = workers
        self._workers_on_free_day = workers_on_free_day

    def __str__(self) -> str:
        return f"Firma transportowa '{self._company_name}', właściciel: '{self._owner_name}', założona w roku: " + \
               f"{self._year_of_start}, przy ul. {self._address_street}, {self._address_postal} {self._address_city}, " + \
               f"wartość firmy: {self._company_value_in_mil} milionów PLN, liczba samochodów: {self._number_of_cars}, " + \
               f"zasięg firmy: {self._max_delivery_range_in_km} km, pracowników: {self._workers}, liczba pracowników " + \
               f"na urlopie: {self._workers_on_free_day}."