from models.dieta import Dieta
from models.dietetyk import Dietetyk
from models.pacjent import Pacjent
from models.zamowienie import Zamowienie


dieta_1 = Dieta("dieta wegańska", "zwyczajna", True, True, 1200, 100.50)
dieta_2 = Dieta("dieta wegetariańska", "zwyczajna", True, False, 1800, 134.54)
dieta_3 = Dieta("dieta mięsna", "dziwna", False, False, 5000, 444.22)
dietetyk_1 = Dietetyk("Andrzej", "Odchudzacz", "ART001", True)
pacjent_1 = Pacjent("Władysław", "Grubasek", "KLI001", True)

zamowienie_1 = Zamowienie("", "", 0, False, [], None, None)
zamowienie_1.nr_zamowienia = "ZAM001"
zamowienie_1.data_zamowienia = "2022-01-15"
zamowienie_1.oplacone = False
zamowienie_1.pacjent = pacjent_1
zamowienie_1.dietetyk = dietetyk_1
zamowienie_1.dieta = dieta_1
zamowienie_1.dieta = dieta_2
zamowienie_1.dieta = dieta_3
zamowienie_1.wartosc_zamowienia = zamowienie_1.sumuj_wartosc_zamowienia()

print(zamowienie_1)
