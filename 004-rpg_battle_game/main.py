from colorama import init
from src.constants import bcolors
from src.game import enemy_round, init_game, generate_enemies, generate_players, display_stats, player_round

players = generate_players()
enemies = generate_enemies()

running = True
i = 0

init()
init_game()

while running:

    # Players' Round
    for player in players:
        display_stats(players=players, enemies=enemies)
        player, players, enemies = player_round(player=player, players=players, enemies=enemies)
    
    print("")

    # Check if all enemies are dead and end the game
    if len(enemies) == 0:
        print(bcolors.OKGREEN + "You win! All enemies have been defeated." + bcolors.ENDC)
        running = False
        break

    # Enemies' Round
    for enemy in enemies:
        enemy, players, enemies = enemy_round(enemy=enemy, players=players, enemies=enemies)

    print("")

    # Check if all players are dead and end the game
    if len(players) == 0:
        print(bcolors.FAIL + "All players are dead." + bcolors.ENDC)
        running = False