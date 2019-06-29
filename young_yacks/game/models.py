from typing import List


class EarthSystem:
    name: str
    unit: str
    min: float
    max: float
    current_value: float


class CowBreed:
    name: str
    upgrade_level: int
    value: float
    water_pollution_rate: float
    greenhouse_gas_rate: float
    cost: float
    total_cows: int


class Farm:
    income: float
    cow_types: List[CowBreed]
    systems: List[EarthSystem]

    @staticmethod
    def get_income_rate(cow_breeds: List[CowBreed]) -> float: pass

    @staticmethod
    def get_environment_damage_rate(cow_breeds: List[CowBreed], systems: List[EarthSystem]) -> List[EarthSystem]: pass


class Game:
    farm: Farm
    has_won: bool
    doomed_win_perc: float
