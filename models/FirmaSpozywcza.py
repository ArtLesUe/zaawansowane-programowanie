from models.Firma import Firma


class FirmaSpozywcza(Firma):
    def __init__(self, company_name: str, owner_name: str, year_of_start: int, address_street: str,
                 address_postal: str, address_city: str, type_of_goods: str, max_cargo_one_transport: int,
                 have_forklift: bool, premium_service: bool, unpaid_invoices: bool) -> None:
        super().__init__(company_name, owner_name, year_of_start, address_street, address_postal, address_city)
        self._type_of_goods = type_of_goods
        self._max_cargo_one_transport = max_cargo_one_transport
        self._have_forklift = have_forklift
        self._premium_service = premium_service
        self._unpaid_invoices = unpaid_invoices

    def __str__(self) -> str:
        return f"Firma spożywcza '{self._company_name}', właściciel: '{self._owner_name}', założona w roku: " + \
            f"{self._year_of_start}, przy ul. {self._address_street}, {self._address_postal} {self._address_city}, " + \
            f"handluje towarem: '{self._type_of_goods}', maksymalny odbiór towaru: {self._max_cargo_one_transport} kg," + \
            f"czy posiadają wózek widłowy: {self._have_forklift}, usługa premium: {self._premium_service}, " + \
            f"czy ma niezapłacone faktury: {self._unpaid_invoices}."