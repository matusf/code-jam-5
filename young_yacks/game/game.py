from models import CowBreed, EarthSystem, Player


class WaterSystem(EarthSystem):
    unit = 'level'
    min = 0
    max = 100
    # Above avegage
    current_value = 0


class AirSystem(EarthSystem):
    min = 0
    max = 100
    unit = 'degree Celsius'
    current_value = 0


class MeatCowBreed(CowBreed):
    damage_rates = {
        WaterSystem: 10,
        EarthSystem: 15,
    }
    cost = 80


class MilkCowBreed(CowBreed):
    damage_rates = {
        WaterSystem: 20,
        EarthSystem: 5,
    }
    cost = 100


class BurpCowBreed(CowBreed):
    damage_rates = {
        WaterSystem: 15,
        EarthSystem: 30,
    }
    total_cows = 0
    cost = 150


class Game:
    def __init__(self):
        self.player = Player()
