from datetime import datetime


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


class Odcinek:
    def __init__(self, city_start: str, city_end, road_length_km: int, is_paid: bool, planned_time_mins: int) -> None:
        self._city_start = city_start
        self._city_end = city_end
        self._road_length_km = road_length_km
        self._is_paid = is_paid
        self._planned_time_mins = planned_time_mins
        pass

    @property
    def road_length_km(self) -> int:
        return self._road_length_km

    def __str__(self) -> str:
        return f"Odcinek trasy z {self._city_start} do {self._city_end} o długości {self._road_length_km} km, " + \
            f"czy zawiera odcinki płatne: '{self._is_paid}', długość trasy: {self._planned_time_mins} minut"


class Kurs:
    def __init__(self) -> None:
        self._date_start = None
        self._date_end = None
        self._used_car = None
        self._start_company = None
        self._end_company = None
        self._road_plan = list()

    @property
    def date_start(self) -> datetime:
        return self._date_start

    @property
    def date_end(self) -> datetime:
        return self._date_end

    @property
    def used_car(self) -> Pojazd:
        return self._used_car

    @property
    def start_company(self) -> FirmaTransportowa:
        return self._start_company

    @property
    def end_company(self) -> FirmaSpozywcza:
        return self._end_company

    @property
    def road_plan(self) -> list:
        return [ plan for plan in self._road_plan ]

    @date_start.setter
    def date_start(self, value: datetime):
        self._date_start = value

    @date_end.setter
    def date_end(self, value: datetime):
        self._date_end = value

    @used_car.setter
    def used_car(self, value: Pojazd):
        self._used_car = value

    @start_company.setter
    def start_company(self, value: FirmaTransportowa):
        self._start_company = value

    @end_company.setter
    def end_company(self, value: FirmaSpozywcza):
        self._end_company = value

    @road_plan.setter
    def road_plan_add(self, value: Odcinek):
        self._road_plan.append(value)

    def calculate_course_length(self) -> float:
        return [ round(sum(part.road_length_km()), 2) for part in self._road_plan ]

    def get_used_car_mark(self) -> str:
        return self._used_car.car_mark()

    def __str__(self) -> str:
        return f"Zlecony kurs z firmy transportowej '{self._start_company}' do firmy spożywczej '{self._end_company}', " + \
            f"został zaplanowany w terminie od {self._date_start} do {self._date_end}, przy pomocy pojazdu " + \
            f"'{self._used_car}', długość trasy na wszystkich odcinkach to: {self.calculate_course_length} km, " + \
            f"marka pojazdu użyta do transportu to '{self.get_used_car_mark}'."
        pass


company_1 = FirmaTransportowa("Artur Transport", "Artur Leśnik", 2010, "ul. Katowicka 112", "00-000", "Katowice",
                              100, 50, 500, 100, 10)
company_2 = FirmaSpozywcza("Buraki Magazyn", "Jan testowy", 2015, "ul. Gliwicka 12", "00-000", "Gliwice", "buraki",
                           1000, False, False, True)

car_1 = Pojazd("SR 123456", 1000, 200, 2006, datetime.now(), "Toyota", company_1)

part_1 = Odcinek("Rybnik", "Katowice", 50, False, 60)
part_2 = Odcinek("Katowice", "Gliwice", 40, True, 45)

course_1 = Kurs()
course_1.date_start = datetime.today()
course_1.date_end = datetime.today()
course_1.used_car = car_1
course_1.start_company = company_1
course_1.end_company = company_2
course_1.road_plan_add = part_1
course_1.road_plan_add = part_2

print(course_1)