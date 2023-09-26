from car import Car
from engines.sternman_engine import SternmanEngine
from batteries.spindler_battery import SpindlerBattery
from tires.octoprime_tire import OctoprimeTire


class Palindrome(Car):
    def __init__(self, last_service_date, warning_light, tire_sensor_data):
        super().__init__(
            last_service_date,
            SternmanEngine(warning_light),
            SpindlerBattery(last_service_date),
            OctoprimeTire(tire_sensor_data),
        )

    def needs_service(self):
        return super().needs_service()
