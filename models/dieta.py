class Dieta:
    def __init__(self, nazwa: str, rodzaj: str, czy_wegetarianska: bool, czy_weganska: bool,
                 kcal: int, cena: float) -> None:
        self._nazwa = nazwa
        self._rodzaj = rodzaj
        self._czy_wegetarianska = czy_wegetarianska
        self._czy_weganska = czy_weganska
        self._kcal = kcal
        self._cena = cena

    def __str__(self) -> str:
        return f"Dieta o nazwie {self._nazwa}, rodzaju {self._rodzaj}, jest dietą wegetariańską: " + \
            f"{self._czy_wegetarianska}, jest dietą wegańską: {self._czy_weganska}, kcal: {self._kcal}, " + \
            f"cena diety: {self._cena} zł"

    @property
    def nazwa(self) -> str:
        return self._nazwa

    @property
    def rodzaj(self) -> str:
        return self._rodzaj

    @property
    def czy_wegetarianska(self) -> bool:
        return self._czy_wegetarianska

    @property
    def czy_weganska(self) -> bool:
        return self._czy_weganska

    @property
    def kcal(self) -> int:
        return self._kcal

    @property
    def cena(self) -> float:
        return self._cena
