from tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, tire_sensor_data):
        super().__init__(tire_sensor_data)

    def needs_service(self):
        return sum(self.tire_sensor_data) >= 3.0
