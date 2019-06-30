from cowbreed import CowBreed
from earth_system import EarthSystem
from typing import List


class Player:
    money: float
    cow_types: List[CowBreed]
    systems: List[EarthSystem]
    win_threshold: int
    lose_threshold: int  # must be higher than win_threshold

    @staticmethod
    def get_income(cow_breeds: List[CowBreed], dt: float) -> float:
        pass

    @staticmethod
    def get_environment_damage_rate(
            cow_breeds: List[CowBreed], systems: List[EarthSystem], dt: float) -> List[EarthSystem]:
        pass

    @staticmethod
    def get_doomed_perc(systems: List[EarthSystem]) -> int:
        pass

    @staticmethod
    def has_won(doom_perc: int, win_thereshold: int, game_time: float, ) -> bool:
        pass

    @staticmethod
    def has_lost(max_doom_perc: int, lose_threshold: int) -> bool:
        pass


# class Game:
#    player: Player
#    game_time: float
#    cow_breeds: List[CowBreed]
