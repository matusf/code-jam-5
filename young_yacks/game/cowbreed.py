class CowBreed:
    name: str
    value: float
    damage_rates: Dict[EarthSystem: int]
    cost: float
    total_cows: int

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