from typing import List, Dict


class Environment():
    def __init__(self, name: str, level: float, unit: str, min_value: float, max_value: float):
        """ Stores info on the earths environments, like it's air."""
        self.name = name
        self.level = level
        self.unit = unit
        self.min_value = min_value
        self.max_value = max_value

    @property
    def level_perc(self) -> float:
        """Returns the level's percentage between the min and max values"""
        return (self.level - self.min) / (self.max - self.min)


class CowBreed():
    def __init__(self, name: str, damage_rates: Dict[Environment, int],
                 value: float, cost: float, total_cows: int = 0):
        self.name = name
        self.damage_rates = damage_rates
        self.value = value
        self.cost = cost
        self.total_cows = total_cows


class Game:
    """ The object which stores all info needed for the game."""
    def __init__(self, game_time: float, win_threshold: float, lose_threshold: float,
                 money: float, cows: List[CowBreed], environments: List[Environment]):
        self.game_time = game_time
        self.win_threshold = win_threshold
        self.lose_threshold = lose_threshold
        self.money = money or 0
        self.cows = cows
        self.environments = environments

    @classmethod
    def init_game(cls):
        """Instantiates all game models and returns a new Game."""

        water_level = Environment(name='Water Level', unit='m', min=20, max=22, level=20.5)
        temperature = Environment(name='Air Temperature', unit='°C', min=10, max=40, level=15)

        meat_cows = CowBreed(name="Meat Cows", damage_rates={water_level: 10, temperature: 15},
                             value=20, cost=100)
        milk_cows = CowBreed(name="Milk Cows", damage_rates={water_level: 20, temperature: 5},
                             value=30, cost=150)
        burp_cows = CowBreed(name="Burp Cows", damage_rates={water_level: 5, temperature: 50},
                             value=40, cost=30)
        return cls(game_time=120, win_threshold=0.7, lose_threshold=0.9, money=0, cows=[meat_cows,
                   milk_cows, burp_cows], environment=[water_level, temperature])

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
        """The earth's overall damage, between 0 (unharmed) and 1 (harmed).
        Based on contributions from each system."""
        damage = sum(system.level_perc for system in Environment.all()) / len(Environment.all())
        assert 0 <= damage <= 1
        return damage

    @property
    def was_won(self) -> bool:
        return (self.game_time <= 0 and
                self.win_threshold < self.earth_damage_perc < self.lose_threshold)

    @property
    def was_lost(self):
        return (self.earth_damage_perc > self.lose_threshold
                or (self.game_time < 0. and not self.was_won))
