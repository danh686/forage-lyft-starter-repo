from car import Car
from engines.willoughby_engine import WilloughbyEngine
from batteries.spindler_battery import SpindlerBattery
from tires.carrigan_tire import CarriganTire


class Glissade(Car):
    def __init__(
        self, curent_mileage, last_service_date, last_service_mileage, tire_sensor_data
    ):
        super().__init__(
            last_service_date,
            WilloughbyEngine(curent_mileage, last_service_mileage),
            SpindlerBattery(last_service_date),
            CarriganTire(tire_sensor_data),
        )

    def needs_service(self):
        return super().needs_service()
