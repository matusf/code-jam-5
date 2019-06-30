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
        return rules.get_system_damage_perc(system=self)


@dataclass
class CowBreed:
    name: str
    damage_rates: Dict[EarthMetric, int] = field(repr=False)
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
    def damages(self) -> Dict[EarthMetric, float]:
        """The rate of damage on each systems, when all cows are taken into account."""
        return rules.get_environment_damage(cow_breeds=self.cows, systems=self.systems)

    @property
    def earth_damage_perc(self) -> float:
        """The earth's overall damage level, between 0 (unharmed) and 1 (harmed)."""
        return rules.get_earth_damage_perc(systems=self.systems)


class Game:
    player: Player
    game_time: float
    cow_breeds: List[CowBreed]

    @property
    def was_won(self) -> bool:
        return rules.player_scared_aliens(
            doom_perc=self.player.earth_damage_perc,
            win_threshold=self.player.win_threshold,
            lose_threshold=self.player.lose_threshold,
            game_time=self.game_time
        )

    @property
    def was_lost(self):
        lost1 = rules.player_destroyed_earth(
            doom_perc=self.player.earth_damage_perc,
            lose_threshold=self.player.lose_threshold,
        )
        out_of_time = self.game_time < 0.
        return lost1 or out_of_time
