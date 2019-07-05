import threading
from random import random, randint
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
        return (self.level - self.min_value) / (self.max_value - self.min_value)


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
                 money: float, cows: Dict[str, CowBreed], environments: List[Environment]):
        self.game_time = game_time
        self.win_threshold = win_threshold
        self.lose_threshold = lose_threshold
        self.money = money or 0
        self.cows = cows
        self.environments = environments
        self.breed()

    @classmethod
    def init_game(cls):
        """Instantiates all game models and returns a new Game."""

        water_level = Environment(name='Water Level', unit='m', min_value=20, max_value=22, level=20.5)
        temperature = Environment(name='Air Temperature', unit='°C', min_value=10, max_value=40, level=15)

        meat_cows = CowBreed(name="Meat Cows", damage_rates={water_level: 10, temperature: 15},
                             value=20, cost=100)
        milk_cows = CowBreed(name="Milk Cows", damage_rates={water_level: 20, temperature: 5},
                             value=30, cost=150)
        burp_cows = CowBreed(name="Burp Cows", damage_rates={water_level: 5, temperature: 50},
                             value=40, cost=30)

        cows = {cow.name: cow for cow in (meat_cows, milk_cows, burp_cows)}
        return cls(game_time=120, win_threshold=0.7, lose_threshold=0.9, money=0, cows=cows, environments=[water_level, temperature])

    @property
    def income(self):
        """The player's income rate."""
        return sum(breed.value * breed.total_cows for breed in self.cows.values())

    @property
    def damages(self) -> Dict[Environment, float]:
        """The rate of damage on each system, when all cows are taken into account."""
        damage = {}
        for system in self.environments:
            damage[system.name] = sum(breed.damage_rates[system] for breed in self.cows.values())
        return damage

    @property
    def earth_damage_perc(self) -> float:
        """The earth's overall damage, between 0 (unharmed) and 1 (harmed).
        Based on contributions from each system."""
        damage = sum(system.level_perc for system in self.environments) / len(self.environments)
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

    def buy_cow(self, breed, number=1):
        breed = self.cows[breed]
        if breed.cost * number > self.money:
            raise ValueError('Not enough money')

        self.cows[breed].total_cows += number
        self.money -= breed.cost * number

    def sell_cow(self, breed, number=1):
        """Sell cow for 40% of the original value"""
        if self.cows[breed].total_cows > number:
            raise ValueError('Not enough cows')

        self.cows[breed].total_cows -= number
        self.money += number * self.cows[breed].cost * .4

    def update(self, delta_time):
        self.game_time -= delta_time

    def breed(self):
        """There is a 25% chance for every cow breed to breed. Their number will 
        increase in range from 0 to 1/4 of they current population.
        
        This function calls itselt every 20 seconds. It stops when game ends.
        """
        for breed in self.cows:
            if random() <= .25: 
                self.cows[breed].total_cows += randint(0, self.cows[breed].total_cows // 4)
        
        if self.game_time >= 0 and (not self.was_lost):
            threading.Timer(20, self.breed)
