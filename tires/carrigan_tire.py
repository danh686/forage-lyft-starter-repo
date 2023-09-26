from tire import Tire


class CarriganTire(Tire):
    def __init__(self, tire_sensor_data):
        super().__init__(tire_sensor_data)

    def needs_service(self):
        return any(map(lambda current_tire: current_tire >= 0.9, self.tire_sensor_data))
