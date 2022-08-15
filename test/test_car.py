import unittest
from datetime import datetime

from battery.spindler_battery import SpindlerBattery
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine


class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        capulet = CapuletEngine(current_mileage, last_service_mileage)
        spindler = SpindlerBattery(last_service_date, current_date)
        car = Car(capulet, spindler)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        capulet = CapuletEngine(current_mileage, last_service_mileage)
        spindler = SpindlerBattery(last_service_date, current_date)
        car = Car(capulet, spindler)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date
        current_mileage = 30001
        last_service_mileage = 0

        capulet = CapuletEngine(current_mileage, last_service_mileage)
        spindler = SpindlerBattery(last_service_date, current_date)
        car = Car(capulet, spindler)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date
        current_mileage = 30000
        last_service_mileage = 0

        capulet = CapuletEngine(current_mileage, last_service_mileage)
        spindler = SpindlerBattery(last_service_date, current_date)
        car = Car(capulet, spindler)
        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        capulet = WilloughbyEngine(current_mileage, last_service_mileage)
        spindler = SpindlerBattery(last_service_date, current_date)
        car = Car(capulet, spindler)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        capulet = WilloughbyEngine(current_mileage, last_service_mileage)
        spindler = SpindlerBattery(last_service_date, current_date)
        car = Car(capulet, spindler)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date
        current_mileage = 60001
        last_service_mileage = 0

        capulet = WilloughbyEngine(current_mileage, last_service_mileage)
        spindler = SpindlerBattery(last_service_date, current_date)
        car = Car(capulet, spindler)
        self.assertTrue(car.needs_service())


    def test_engine_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date
        current_mileage = 60000
        last_service_mileage = 0

        capulet = WilloughbyEngine(current_mileage, last_service_mileage)
        spindler = SpindlerBattery(last_service_date, current_date)
        car = Car(capulet, spindler)
        self.assertFalse(car.needs_service())

if __name__ == '__main__':
    unittest.main()
