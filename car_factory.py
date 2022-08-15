from datetime import date

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class CarFactory():
    # capuet, spindler
    def create_calliope(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        capulet = CapuletEngine(current_mileage, last_service_mileage)
        spindler = SpindlerBattery(last_service_date, current_date)
        car = Car(capulet, spindler)
        return car

    def create_glissade(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        willoughbyEngine = WilloughbyEngine (current_mileage, last_service_mileage)
        spindler = SpindlerBattery(last_service_date, current_date)
        car = Car(willoughbyEngine, spindler)
        return car

    def create_palindrome(self, current_date: date, last_service_date: date, warning_light_on: bool):
        sternman = SternmanEngine(warning_light_on)
        spindler = SpindlerBattery(last_service_date, current_date)
        car = Car(sternman, spindler)
        return car

    def create_rorschach(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        willoughbyEngine = WilloughbyEngine(current_mileage, last_service_mileage)
        nubbin = NubbinBattery(last_service_date, current_date)
        car = Car(willoughbyEngine, nubbin)
        return car

    def create_thovex(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        capulet = CapuletEngine(current_mileage, last_service_mileage)
        nubbin = NubbinBattery(last_service_date, current_date)
        car = Car(capulet, nubbin)
        return car


