from models.dieta import Dieta
from models.dietetyk import Dietetyk
from models.pacjent import Pacjent


class Zamowienie:
    def __init__(self, nr_zamowienia: str, data_zamowienia: str, wartosc_zamowienia: float, oplacone: bool,
                 dieta: list, pacjent: Pacjent, dietetyk: Dietetyk) -> None:
        self._nr_zamowienia = nr_zamowienia
        self._data_zamowienia = data_zamowienia
        self._wartosc_zamowienia = wartosc_zamowienia
        self._oplacone = oplacone
        self._dieta = dieta
        self._pacjent = pacjent
        self._dietetyk = dietetyk

    def __str__(self) -> str:
        return f"Zamówienie o numerze {self._nr_zamowienia}, z dnia {self._data_zamowienia}, na kwotę " + \
            f"{self._wartosc_zamowienia:.2f} zł, opłacone: {self._oplacone}, zawiera przepis na diety: '" + \
            f"{self.dieta}' przepisane przez '{self._dietetyk}', dla pacjenta '{self._pacjent}', suma " + \
            f"kalorii {self.sumuj_kalorie()} kcal."

    @property
    def nr_zamowienia(self) -> str:
        return self._nr_zamowienia

    @property
    def data_zamowienia(self) -> str:
        return self._data_zamowienia

    @property
    def wartosc_zamowienia(self) -> float:
        return self._wartosc_zamowienia

    @property
    def oplacone(self) -> bool:
        return self._oplacone

    @property
    def dieta(self) -> list:
        return [dieta.__str__() for dieta in self._dieta]

    @property
    def pacjent(self) -> Pacjent:
        return self._pacjent

    @property
    def dietetyk(self) -> Dietetyk:
        return self._dietetyk

    @nr_zamowienia.setter
    def nr_zamowienia(self, wartosc: str) -> None:
        self._nr_zamowienia = wartosc

    @data_zamowienia.setter
    def data_zamowienia(self, wartosc: str) -> None:
        self._data_zamowienia = wartosc

    @wartosc_zamowienia.setter
    def wartosc_zamowienia(self, wartosc: float) -> None:
        self._wartosc_zamowienia = wartosc

    @oplacone.setter
    def oplacone(self, wartosc: bool) -> None:
        self._oplacone = wartosc

    @dieta.setter
    def dieta(self, wartosc: Dieta) -> None:
        self._dieta.append(wartosc)

    @pacjent.setter
    def pacjent(self, wartosc: Pacjent) -> None:
        self._pacjent = wartosc

    @dietetyk.setter
    def dietetyk(self, wartosc: Dietetyk) -> None:
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
