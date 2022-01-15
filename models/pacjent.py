class Pacjent:
    def __init__(self, imie: str, nazwisko: str, numer_klienta: str, ma_abonament: bool) -> None:
        self._imie = imie
        self._nazwisko = nazwisko
        self._numer_klienta = numer_klienta
        self._ma_abonament = ma_abonament

    def __str__(self) -> str:
        return f"Pacjent {self._imie} {self._nazwisko}, o numerze {self._numer_klienta}, " + \
               f"posiada abonament: {self._ma_abonament}"

    @property
    def imie(self) -> str:
        return self._imie

    @property
    def nazwisko(self) -> str:
        return self._nazwisko

    @property
    def numer_klienta(self) -> str:
        return self._numer_klienta

    @property
    def ma_abonament(self) -> bool:
        return self._ma_abonament
