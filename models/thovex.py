from car import Car
from engines.capulet_engine import CapuletEngine
from batteries.nubbin_battery import NubbinBattery


class Thovex(Car):
    def __init__(self, current_mileage, last_service_mileage, last_service_date):
        super().__init__(
            self,
            last_service_date,
            CapuletEngine(current_mileage, last_service_mileage),
            NubbinBattery(last_service_date),
        )

    def needs_service(self):
        return super().needs_service()
