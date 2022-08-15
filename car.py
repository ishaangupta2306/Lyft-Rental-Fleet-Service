from abc import abstractmethod
from serviceable import Serviceable
from engine.engine import EngineInterface
from battery.battery import BatteryInterface

class Car(Serviceable):
    def __init__(self, engine: EngineInterface, battery: BatteryInterface):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()
