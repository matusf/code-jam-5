from typing import List, Dict
from dataclasses import dataclass, field
from . import rules

@dataclass
class EarthMetric:
    name: str
    unit: str
    min: float = field(repr=False)
    max: float = field(repr=False)
    current_value: float

    @property
    def damage_perc(self) -> float:
        """Returns the value's percentage between the min and max values"""
        return (self.current_value - self.min) / (self.max - self.min)


@dataclass
class CowBreed:
    name: str
    damage_rates: Dict[EarthMetric: int] = field(repr=False)
    value: float
    cost: float
    total_cows: int = field(default=0)


@dataclass
class Player:
    systems: List[EarthMetric] = field(repr=False)
    win_threshold: int = field(repr=False)
    lose_threshold: int = field(repr=False)  # must be higher than win_threshold
    money: float = field(default=0)
    cows: List[CowBreed] = field(default_factory=list)

    @property
    def income(self):
        """The player's income rate."""
        return rules.get_income(cow_breeds=self.cows)

    @property
    def damages(self) -> Dict[EarthMetric: float]:
        """The rate of damage on each systems, when all cows are taken into account."""
        return rules.get_environment_damage(cow_breeds=self.cows, systems=self.systems)

    @property
    def earth_damage_perc(self) -> float:
        """The earth's overall damage level, between 0 (unharmed) and 1 (harmed)."""
        return rules.get_earth_damage_perc(systems=self.systems)

    @staticmethod
    def has_won(doom_perc: int, win_threshold: int, game_time: float) -> bool:
        pass

    @staticmethod
    def has_lost(max_doom_perc: int, lose_threshold: int) -> bool:
        pass


class Game:
    player: Player
    game_time: float
    cow_breeds: List[CowBreed]
