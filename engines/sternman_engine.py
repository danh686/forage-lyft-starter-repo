from engine import Engine


class SternmanEngine(Engine):
    def __init__(self, warning_light):
        super().__init__(0, 0, warning_light=warning_light)
        self.warning_light = warning_light

    def needs_service(self):
        if self.warning_light:
            return True
        else:
            return False
