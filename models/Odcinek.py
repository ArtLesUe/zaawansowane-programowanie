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