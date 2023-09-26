from car import Car
from engines.capulet_engine import CapuletEngine
from batteries.spindler_battery import SpindlerBattery
from tires.octoprime_tire import OctoprimeTire


class Calliope(Car):
    def __init__(
        self, current_mileage, last_service_mileage, last_service_date, tire_sensor_data
    ):
        super().__init__(
            last_service_date,
            CapuletEngine(current_mileage, last_service_mileage),
            SpindlerBattery(last_service_date),
            OctoprimeTire(tire_sensor_data),
        )

    def needs_service(self):
        return super().needs_service()
