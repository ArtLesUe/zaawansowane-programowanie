from datetime import datetime

from models.FirmaTransportowa import FirmaTransportowa
from models.Pojazd import Pojazd
from models.FirmaSpozywcza import FirmaSpozywcza
from models.Odcinek import Odcinek


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
        return [plan for plan in self._road_plan]

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
        return [round(sum(part.road_length_km()), 2) for part in self._road_plan]

    def get_used_car_mark(self) -> str:
        return self._used_car.car_mark()

    def __str__(self) -> str:
        return f"Zlecony kurs z firmy transportowej '{self._start_company}' do firmy spożywczej '{self._end_company}', " + \
            f"został zaplanowany w terminie od {self._date_start} do {self._date_end}, przy pomocy pojazdu " + \
            f"'{self._used_car}', długość trasy na wszystkich odcinkach to: {self.calculate_course_length} km, " + \
            f"marka pojazdu użyta do transportu to '{self.get_used_car_mark}'."
        pass