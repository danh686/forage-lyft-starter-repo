from car import Car
from engines.willoughby_engine import WilloughbyEngine
from batteries.nubbin_battery import NubbinBattery
from tires.octoprime_tire import OctoprimeTire


class Rorschach(Car):
    def __init__(
        self, current_mileage, last_service_mileage, last_service_date, tire_sensor_data
    ):
        super().__init__(
            last_service_date,
            WilloughbyEngine(current_mileage, last_service_mileage),
            NubbinBattery(last_service_date),
            OctoprimeTire(tire_sensor_data),
        )

    def needs_service(self):
        return super().needs_service()
