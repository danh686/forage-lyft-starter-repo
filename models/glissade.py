from car import Car
from engines.willoughby_engine import WilloughbyEngine
from batteries.spindler_battery import SpindlerBattery


class Glissade(Car):
    def __init__(self, curent_mileage, last_service_date, last_service_mileage):
        super().__init__(
            last_service_date,
            WilloughbyEngine(curent_mileage, last_service_mileage),
            SpindlerBattery(last_service_date),
        )

    def needs_service(self):
        return super().needs_service()
