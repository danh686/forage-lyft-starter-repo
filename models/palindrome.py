from car import Car
from engines.sternman_engine import SternmanEngine
from batteries.spindler_battery import SpindlerBattery


class Palindrome(Car):
    def __init__(self, last_service_date, warning_light):
        super().__init__(
            last_service_date,
            SternmanEngine(warning_light),
            SpindlerBattery(last_service_date),
        )

    def needs_service(self):
        return super().needs_service()
