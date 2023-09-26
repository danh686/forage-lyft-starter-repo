from car import Car
from engines.capulet_engine import CapuletEngine
from batteries.nubbin_battery import NubbinBattery
from tires.carrigan_tire import CarriganTire


class Thovex(Car):
    def __init__(
        self, current_mileage, last_service_mileage, last_service_date, tire_sensor_data
    ):
        super().__init__(
            last_service_date,
            CapuletEngine(current_mileage, last_service_mileage),
            NubbinBattery(last_service_date),
            CarriganTire(tire_sensor_data),
        )

    def needs_service(self):
        return super().needs_service()
