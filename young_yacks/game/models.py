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
    income_rate: int
    water_pollution_rate: int
    greenhouse_gas_rate: int
    cost: int
    total_cows: int


class Farm:
    income: int
    cow_types: List[CowBreed]
    systems: List[EarthSystem]

    @staticmethod
    def calculate_income(cow_breeds: List[CowBreed]) -> int: pass

    @staticmethod
    def calculate_environment_damage(cow_breeds: List[CowBreed], systems: List[EarthSystem]) -> List[EarthSystem]: pass


class Game:
    farm: Farm
    has_won: bool
    doomed_win_perc: float
