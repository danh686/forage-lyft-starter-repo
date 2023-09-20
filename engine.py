from abc import ABC, abstractmethod


class Engine(ABC):
    def __init__(self, current_mileage, last_service_mileage, warning_light=False):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.warning_light = warning_light

    @abstractmethod
    def needs_service(self):
        pass
