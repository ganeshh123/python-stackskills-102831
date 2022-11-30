from .magic import Spell
from .inventory import Item

actions = ["Attack", "Magic", "Items"]

# Attack Magic Spells
fire = Spell("Fire", 10, 100, "attack")
thunder = Spell("Thunder", 12, 200, "attack")
blizzard = Spell("Blizzard", 16, 400, "attack")
meteor = Spell("Meteor", 20, 500, "attack")
quake = Spell("Quake", 14, 300, "attack")

# Restoration Magic Spells
cure = Spell("Cure", 12, 400, "restoration")
cura = Spell("Cura", 18, 800, "restoration")

# Create Items
potion = Item("Potion", "potion", "Heals 300 HP", 300)
hipotion = Item("Hi-Potion", "potion", "Heals 500 HP", 500)
superpotion = Item("Super Potion", "potion", "Heals 1500 HP", 1500)
elixir = Item("Elixir", "elixir", "Fully restores HP and MP of one party member", 9999)
hielixir = Item("MegaElixir", "elixir", "Fully restores party's HP and MP", 10000)

grenade = Item("Grenade", "attack", "Deals 800 damage", 800)

player_magic = [fire, thunder, blizzard, meteor, cure, cura]
enemy_magic = [fire, meteor, cure]
player_items =  [{'item': potion, 'quantity': 4},
                 {'item': hipotion, 'quantity': 2},
                 {'item': superpotion, 'quantity': 1},
                 {'item': elixir, 'quantity': 3},
                 {'item': hielixir, 'quantity': 1},
                 {'item': grenade, 'quantity': 5}]


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


sep = "================================================================================"
enemy_tag = bcolors.BOLD + "ENEMY:" + bcolors.ENDC
