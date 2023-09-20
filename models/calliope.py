from car import Car
from engines.capulet_engine import CapuletEngine
from batteries.spindler_battery import SpindlerBattery


class Calliope(Car):
    def __init__(self, current_mileage, last_service_mileage, last_service_date):
        super().__init__(
            last_service_date,
            CapuletEngine(current_mileage, last_service_mileage),
            SpindlerBattery(last_service_date),
        )

    def needs_service(self):
        return super().needs_service()
