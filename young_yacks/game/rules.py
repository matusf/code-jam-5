from typing import List, Dict
from .models import EarthMetric, CowBreed


def get_income(cow_breeds: List[CowBreed]) -> float:
    """Returns the income rate, given a list of cow breeds."""
    return sum(breed.value * breed.total_cows for breed in cow_breeds)


def get_earth_damage_perc(systems: List[EarthMetric]) -> float:
    """Returns the earth's overall damage level, given the damage percentage of each individual system."""
    damage = sum(system.damage_perc for system in systems) / len(systems)
    assert 0 <= damage <= 1
    return damage


def get_environment_damage(cow_breeds: List[CowBreed], systems: List[EarthMetric]) -> Dict[EarthMetric: float]:
    """Returns the rate of damage the player is doing to each system, given a list of cow breeds and systems."""
    damage = {}
    for system in systems:
        damage[system] = sum(breed.damage_rates[system] for breed in cow_breeds)
    return damage

