class Dietetyk:
    def __init__(self, imie: str, nazwisko: str, numer_pracownika: str, specjalista: bool) -> None:
        self._imie = imie
        self._nazwisko = nazwisko
        self._numer_pracownika = numer_pracownika
        self._specjalista = specjalista

    def __str__(self) -> str:
        return f"Dietetyk {self._imie} {self._nazwisko}, o numerze {self._numer_pracownika}, " + \
               f"lekarz specjalista: {self._specjalista}"

    @property
    def imie(self) -> str:
        return self._imie

    @property
    def nazwisko(self) -> str:
        return self._nazwisko

    @property
    def numer_pracownika(self) -> str:
        return self._numer_pracownika

    @property
    def specjalista(self) -> bool:
        return self._specjalista
