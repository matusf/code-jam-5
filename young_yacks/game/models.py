from typing import List, Dict
from dataclasses import dataclass, field


@dataclass(unsafe_hash=True)
class EarthMetric:
    level: float = field(hash=False)
    name: str
    unit: str
    min: float = field(repr=False)
    max: float = field(repr=False)

    @property
    def level_perc(self) -> float:
        """Returns the level's percentage between the min and max values"""
        return (self.level - self.min) / (self.max - self.min)


@dataclass(unsafe_hash=True)
class CowBreed:
    name: str
    damage_rates: Dict[EarthMetric, int] = field(repr=False, hash=False)
    value: float
    cost: float
    total_cows: int = field(default=0, hash=False)


@dataclass
class Player:
    systems: List[EarthMetric] = field(repr=False)
    money: float = field(default=0)
    cows: List[CowBreed] = field(default_factory=list)

    @property
    def income(self):
        """The player's income rate."""
        return sum(breed.value * breed.total_cows for breed in self.cows)

    @property
    def damages(self) -> Dict[EarthMetric, float]:
        """The rate of damage on each system, when all cows are taken into account."""
        damage = {}
        for system in self.systems:
            damage[system] = sum(breed.damage_rates[system] for breed in self.cows)
        return damage

    @property
    def earth_damage_perc(self) -> float:
        """The earth's overall damage, between 0 (unharmed) and 1 (harmed), based on contributions from each system."""
        damage = sum(system.level_perc for system in self.systems) / len(self.systems)
        assert 0 <= damage <= 1
        return damage


@dataclass
class Game:
    player: Player
    game_time: float
    cow_breeds: List[CowBreed] = field(repr=False)
    win_threshold: float
    lose_threshold: float  # must be higher than win_threshold

    @property
    def was_won(self) -> bool:
        return self.game_time <= 0 and self.win_threshold < self.player.earth_damage_perc < self.lose_threshold

    @property
    def was_lost(self):
        return self.player.earth_damage_perc > self.lose_threshold or (self.game_time < 0. and not self.was_won)
