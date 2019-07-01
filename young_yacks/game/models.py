from typing import List, Dict
from dataclasses import dataclass, field
from .mixins import Queryable


@dataclass(unsafe_hash=True)
class Environment(Queryable):
    name: str
    level: float = field(hash=False)
    unit: str
    min: float = field(repr=False)
    max: float = field(repr=False)

    @property
    def level_perc(self) -> float:
        """Returns the level's percentage between the min and max values"""
        return (self.level - self.min) / (self.max - self.min)


@dataclass(unsafe_hash=True)
class CowBreed(Queryable):
    name: str
    damage_rates: Dict[Environment, int] = field(repr=False, hash=False)
    value: float
    cost: float
    total_cows: int = field(default=0, hash=False)


@dataclass
class Game:
    game_time: float
    win_threshold: float
    lose_threshold: float  # must be higher than win_threshold
    money: float = field(default=0)
    cows: List[CowBreed] = field(default_factory=CowBreed.all, repr=False)
    environment: List[Environment] = field(default_factory=Environment.all, repr=False)

    @property
    def income(self):
        """The player's income rate."""
        return sum(breed.value * breed.total_cows for breed in CowBreed.all())

    @property
    def damages(self) -> Dict[Environment, float]:
        """The rate of damage on each system, when all cows are taken into account."""
        damage = {}
        for system in Environment.all():
            damage[system.name] = sum(breed.damage_rates[system] for breed in CowBreed.all())
        return damage

    @property
    def earth_damage_perc(self) -> float:
        """The earth's overall damage, between 0 (unharmed) and 1 (harmed), based on contributions from each system."""
        damage = sum(system.level_perc for system in Environment.all()) / len(Environment.all())
        assert 0 <= damage <= 1
        return damage

    @property
    def was_won(self) -> bool:
        return self.game_time <= 0 and self.win_threshold < self.earth_damage_perc < self.lose_threshold

    @property
    def was_lost(self):
        return self.earth_damage_perc > self.lose_threshold or (self.game_time < 0. and not self.was_won)
