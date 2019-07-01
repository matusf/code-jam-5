from .models import EarthMetric, CowBreed, Game, Player


water_level = EarthMetric(name='Water Level', unit='m', min=20, max=22, level=20.5)
temperature = EarthMetric(name='Air Temperature', unit='°C', min=10, max=40, level=15)

meat_cows = CowBreed(name="Meat Cows", damage_rates={water_level: 10, temperature: 15}, value=20, cost=100)
milk_cows = CowBreed(name="Milk Cows", damage_rates={water_level: 20, temperature: 5}, value=30, cost=150)
burp_cows = CowBreed(name="Milk Cows", damage_rates={water_level: 5, temperature: 50}, value=40, cost=30)


def build_game():
    player = Player(systems=[water_level, temperature],
                    win_threshold=0.7,
                    lose_threshold=0.9,
                    )
    game = Game(player=player,
                game_time=120,
                cow_breeds=[meat_cows, milk_cows, burp_cows]
                )
    return game
