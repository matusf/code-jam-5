from .models import Environment, CowBreed, Game, Game


def init_game():

    # All instances of the Queryable dataclasses can be gotten using the Class.all() method.
    water_level = Environment(name='Water Level', unit='m', min=20, max=22, level=20.5)
    temperature = Environment(name='Air Temperature', unit='°C', min=10, max=40, level=15)

    CowBreed(name="Meat Cows", damage_rates={water_level: 10, temperature: 15}, value=20, cost=100)
    CowBreed(name="Milk Cows", damage_rates={water_level: 20, temperature: 5}, value=30, cost=150)
    CowBreed(name="Milk Cows", damage_rates={water_level: 5, temperature: 50}, value=40, cost=30)

    game = Game(game_time=120, win_threshold=0.7, lose_threshold=0.9)
    return game
