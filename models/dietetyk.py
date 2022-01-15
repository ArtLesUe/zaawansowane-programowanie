class Dietetyk:
    def __init__(self, imie: str, nazwisko: str, numer_pracownika: str, specjalista: bool):
        self._imie = imie
        self._nazwisko = nazwisko
        self._numer_pracownika = numer_pracownika
        self._specjalista = specjalista

    def __str__(self):
        return f"Dietetyk {self._imie} {self._nazwisko}, o numerze {self._numer_pracownika}, " + \
               f"lekarz specjalista: {self._specjalista}"

    @property
    def imie(self):
        return self._imie

    @property
    def nazwisko(self):
        return self._nazwisko

    @property
    def numer_pracownika(self):
        return self._numer_pracownika

    @property
    def specjalista(self):
        return self._specjalista
