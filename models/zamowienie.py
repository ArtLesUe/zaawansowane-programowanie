from models.dieta import Dieta
from models.dietetyk import Dietetyk
from models.pacjent import Pacjent


class Zamowienie:
    def __init__(self, nr_zamowienia: str, data_zamowienia: str, wartosc_zamowienia: float, oplacone: bool,
                 dieta: list, pacjent: Pacjent, dietetyk: Dietetyk):
        self._nr_zamowienia = nr_zamowienia
        self._data_zamowienia = data_zamowienia
        self._wartosc_zamowienia = wartosc_zamowienia
        self._oplacone = oplacone
        self._dieta = dieta
        self._pacjent = pacjent
        self._dietetyk = dietetyk

    def __str__(self):
        return f"Zamówienie o numerze {self._nr_zamowienia}, z dnia {self._data_zamowienia}, na kwotę " + \
            f"{self._wartosc_zamowienia:.2f} zł, opłacone: {self._oplacone}, zawiera przepis na diety: '" + \
            f"{self.dieta}' przepisane przez '{self._dietetyk}', dla pacjenta '{self._pacjent}', suma " + \
            f"kalorii {self.sumuj_kalorie()} kcal."

    @property
    def nr_zamowienia(self):
        return self._nr_zamowienia

    @property
    def data_zamowienia(self):
        return self._data_zamowienia

    @property
    def wartosc_zamowienia(self):
        return self._wartosc_zamowienia

    @property
    def oplacone(self):
        return self._oplacone

    @property
    def dieta(self):
        return [dieta.__str__() for dieta in self._dieta]

    @property
    def pacjent(self):
        return self._pacjent

    @property
    def dietetyk(self):
        return self._dietetyk

    @nr_zamowienia.setter
    def nr_zamowienia(self, wartosc: str):
        self._nr_zamowienia = wartosc

    @data_zamowienia.setter
    def data_zamowienia(self, wartosc: str):
        self._data_zamowienia = wartosc

    @wartosc_zamowienia.setter
    def wartosc_zamowienia(self, wartosc: float):
        self._wartosc_zamowienia = wartosc

    @oplacone.setter
    def oplacone(self, wartosc: bool):
        self._oplacone = wartosc

    @dieta.setter
    def dieta(self, wartosc: Dieta):
        self._dieta.append(wartosc)

    @pacjent.setter
    def pacjent(self, wartosc: Pacjent):
        self._pacjent = wartosc

    @dietetyk.setter
    def dietetyk(self, wartosc: Dietetyk):
        self._dietetyk = wartosc

    def sumuj_wartosc_zamowienia(self) -> float:
        suma: float = 0
        for dieta in self._dieta:
            suma = suma + dieta.cena
        return suma

    def sumuj_kalorie(self) -> int:
        suma: int = 0
        for dieta in self._dieta:
            suma = suma + dieta.kcal
        return suma