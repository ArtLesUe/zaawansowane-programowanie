class Firma:
    def __init__(self, company_name: str, owner_name: str, year_of_start: int, address_street: str,
                 address_postal: str, address_city: str) -> None:
        self._company_name = company_name
        self._owner_name = owner_name
        self._year_of_start = year_of_start
        self._address_street = address_street
        self._address_postal = address_postal
        self._address_city = address_city

    def __str__(self) -> str:
        return f"Firma '{self._company_name}', właściciel: '{self._owner_name}', założona w roku: " + \
               f"{self._year_of_start}, przy ul. {self._address_street}, {self._address_postal} {self._address_city}."