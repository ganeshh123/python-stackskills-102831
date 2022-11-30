import random
from src.player import Player
from src.constants import bcolors, player_magic, player_items, enemy_magic, sep, enemy_tag
from src.utils import cls

def generate_players():
    player1 = Player("Sonic", 2500, 100, 200, 75, player_magic, player_items)
    player2 = Player("Tails", 1000, 150, 100, 30, player_magic, player_items)
    player3 = Player("Knuckles", 4000, 50, 300, 100, player_magic, player_items)

    players = [player1, player2, player3]
    return players


def generate_enemies():
    enemy1 = Player("Eggman", 10000, 700, 525, 25, enemy_magic, [])
    enemy2 = Player("Fang", 1500, 200, 560, 325, enemy_magic, [])
    enemy3 = Player("Metal Sonic", 3000, 50, 560, 325, enemy_magic, [])

    enemies = [enemy1, enemy2, enemy3]
    return enemies

def display_stats(players=[], enemies=[]):
    print(sep)
    if len(players) > 0:
        print(bcolors.BOLD + "PLAYERS:" + bcolors.ENDC + "                         HEALTH                              MAGIC")
        for player in players:
            player.display_stats()
    if len(enemies) > 0:
        print(bcolors.BOLD + "ENEMIES:" + bcolors.ENDC)
        for enemy in enemies:
            enemy.display_stats(enemy=True)
    print(sep)

def init_game():
    print(bcolors.HEADER + bcolors.BOLD + "WELCOME TO PYTHON RPG" + bcolors.ENDC)
    print("To exit, write 'quit' into any prompt and press ENTER.")

def player_round(player, players, enemies):
    player_name = player.get_name()

    action_choice = player.choose_action_player()

    if action_choice == 0:
        dmg = player.generate_damage()

        # Player chooses an enemy to attack
        target_choice = player.choose_target_player(enemies)
        target = enemies[target_choice]
        target_name = target.get_name()
        cls()

        target.take_damage(dmg)
        print(player_name, "attacked", target_name, "for", dmg, "points of damage.")
        if target.get_hp() == 0:
            print(target_name, "was defeated.")
            del enemies[target_choice]
        
    elif action_choice == 1:
        # Player chooses a spell:
        spell_choice = player.choose_magic_player()
        spell = player.magic[spell_choice]
        spell_name = spell.get_name()
        spell_dmg = spell.generate_damage()

        player.reduce_mp(spell.get_cost())

        if spell.get_type() == "restoration":
            # Player chose healing spell
            cls()
            player.heal(spell_dmg)
            print(bcolors.OKBLUE + "\n" + spell_name + " heals", player_name, "for", str(spell_dmg), "HP." + bcolors.ENDC)
        elif spell.get_type() == "attack":
            # Player chose attack spell

            # Player chooses an enemy
            target_choice = player.choose_target_player(enemies)
            target = enemies[target_choice]
            target_name = target.get_name()
            cls()

            target.take_damage(spell_dmg)
            print(bcolors.OKBLUE + "\n" + spell_name + " deals", str(spell_dmg), "points of damage to", target_name + bcolors.ENDC)
            if target.get_hp() == 0:
                print(target_name, "was defeated.")
                del enemies[target_choice]
    
    elif action_choice == 2:
        # Player chooses an item
        item_choice = player.choose_item_player()

        # Reduce Item Quantity
        item_quantity = player.items[item_choice]["quantity"]
        player.items[item_choice]["quantity"] = item_quantity - 1
        
        item = player.items[item_choice]["item"]
        item_name = item.get_name()
        item_strength = item.get_value()
        item_type = item.get_type()
        
        if item_type == "potion":
            cls()
            player.heal(item.get_value())
            print(bcolors.OKGREEN + "\n" + item_name + " heals " + player_name + " for", str(item_strength), "HP" + bcolors.ENDC)
        elif item_type == "elixir":
            cls()
            if item_name == 'MegaElixir':
                # If MegaElixir, restore every player's hp and mana
                for i in players:
                    i.set_hp(i.get_max_hp())
                    i.set_mp(i.get_max_mp())
                print(bcolors.OKGREEN + "\n" + item_name + " fully restores HP/MP of all players." + bcolors.ENDC)
            else:
                # Otherwise restore current player's hp and mana
                player.set_hp(player.get_max_hp())
                player.set_mp(player.get_max_mp())
                print(bcolors.OKGREEN + "\n" + item_name + " fully restores HP/MP." + bcolors.ENDC)
        elif item_type == "attack":
            # Player chooses an enemy
            target_choice = player.choose_target_player(enemies)
            target = enemies[target_choice]
            target_name = target.get_name()
            cls()

            target.take_damage(item_strength)
            print(bcolors.FAIL + "\n" + item_name + " deals", str(item_strength), "points of damage to", target_name + "." + bcolors.ENDC)
            if target.get_hp() == 0:
                print(target_name, "was defeated.")
                del enemies[target_choice]

    return player, players, enemies


def enemy_round(enemy, players, enemies):
    enemy_name = enemy.get_name()
        
    # Choose an action
    action_choice = enemy.choose_action_ai()

    # Choose a player target
    target_choice = random.randrange(0, len(players))
    target = players[target_choice]
    target_name = target.get_name()

    if action_choice == 0:
        dmg = enemy.generate_damage()
        target.take_damage(dmg)
        print(enemy_tag, enemy_name, "attacks", target_name, "for", dmg, "points of damage.")
    
        if target.get_hp() == 0:
            print(target_name, "has died.")
            del players[target_choice]
    elif action_choice == 1:
        spell = enemy.choose_magic_ai()
        spell_name = spell.get_name()
        spell_dmg = spell.generate_damage()
        enemy.reduce_mp(spell.get_cost())
        
        if spell.get_type() == "attack":
            target.take_damage(spell_dmg)
            print(enemy_tag, enemy_name, "attacks",target_name, "with spell", spell_name, "for", spell_dmg, "points of damage.")

            if target.get_hp() == 0:
                print(target_name, "has died.")
                del players[target_choice]
        elif spell.get_type() == "restoration":
            enemy.heal(spell_dmg)
            print(enemy_tag, bcolors.OKBLUE + spell_name + " heals", enemy_name, "for", str(spell_dmg), "HP." + bcolors.ENDC)
        
    return enemy, players, enemies
