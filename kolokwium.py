from datetime import datetime

from models.FirmaSpozywcza import FirmaSpozywcza
from models.FirmaTransportowa import FirmaTransportowa
from models.Pojazd import Pojazd
from models.Odcinek import Odcinek
from models.Kurs import Kurs


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
