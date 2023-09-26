from abc import ABC, abstractmethod

class Tire(ABC):
    def __init__(self, tire_sensor_data):
        self.tire_sensor_data = tire_sensor_data

    @abstractmethod
    def needs_service(self):
        pass