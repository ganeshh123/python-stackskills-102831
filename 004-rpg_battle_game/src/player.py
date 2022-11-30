import random
from .constants import bcolors, actions
from .utils import input_number

class Player:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = actions


    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)


    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp


    def take_damage(self, dmg):
        self.hp = self.hp - dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_name(self):
        return self.name

    def get_hp(self):
        return self.hp


    def set_hp(self, hp):
        self.hp = hp


    def get_max_hp(self):
        return self.maxhp


    def get_hp_percentage(self):
        return self.hp / self.maxhp * 100


    def get_mp(self):
        return self.mp


    def set_mp(self, mp):
        self.mp = mp


    def get_max_mp(self):
        return self.maxmp


    def get_mp_percentage(self):
        return self.mp / self.maxmp * 100


    def reduce_mp(self, cost):
        self.mp = self.mp - cost

    def choose_action_player(self):
        i = 1
        print(bcolors.BOLD + "\nWhat will " + self.name + " do?\n" + bcolors.ENDC)
        print(bcolors.OKBLUE + bcolors.BOLD + "ACTIONS:" + bcolors.ENDC)
        for item in self.actions:
            strength = ''
            if i == 1:
                strength = '(damage in range ' + str(self.atkl) + ' to ' + str(self.atkh) + ')'
            print("    " + str(i) + ".", item, strength)
            i += 1
        return input_number("Choose action: ", 1, i-1) - 1


    def choose_magic_player(self):
        i = 1
        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "MAGIC:" + bcolors.ENDC)
        for spell in self.magic:
            spell_type = spell.get_type()
            spell_description = "Damages target by " + f'{str(spell.get_dmg()-15):4}' + 'to ' + f'{str(spell.get_dmg()+15):4}'
            if spell_type == "restoration":
                spell_description = "Restores health by " + f'{str(spell.get_dmg()-15):4}' + 'to ' + f'{str(spell.get_dmg()+15):4}'
            print("    " + str(i) + ".", f'{spell.get_name():15}', f'{spell_description:30}' , " Cost:", f'{str(spell.get_cost()):4}', " Type:", str(spell_type).capitalize() + "")
            i += 1
        spell_choice = input_number("Choose magic: ", 1, i-1) - 1
        spell = self.magic[spell_choice]
        # If not enough Mana, choose again.
        if spell.get_cost() > self.mp:
            print(bcolors.FAIL + "\nNot enough magic points.\n" + bcolors.ENDC)
            return self.choose_magic_player()
        
        return spell_choice

    def choose_item_player(self):
        i = 1
        print("\n" + bcolors.OKGREEN + bcolors.BOLD + "ITEMS:" + bcolors.ENDC)
        for inventory_item in self.items:
            item = inventory_item["item"]
            print("    " + str(i) + ".", item.get_name(), ":", item.get_description(), "(x" + str(inventory_item["quantity"]) + ")")
            i += 1
        item_choice = input_number("Choose item: ", 1, i-1) - 1
        item_quantity = self.items[item_choice]["quantity"]
        if item_quantity == 0:
            print(bcolors.FAIL + "\n" + "None left..." + bcolors.ENDC)
            return self.choose_item_player()
        
        return item_choice

    def choose_target_player(self, enemies):
        i = 1
        print("\n" + bcolors.FAIL + bcolors.BOLD + "TARGET:" + bcolors.ENDC)
        for enemy in enemies:
            if enemy.get_hp() != 0:
                print("    " + str(i) + "." + enemy.get_name())
                i += 1
        return input_number("Choose target: ", 1, i-1) - 1

    def choose_action_ai(self):
        if self.get_hp_percentage() < 30 & len(self.magic) > 0:
            # If health is below 30 percent, look for a healing spell first
            for spell in self.magic:
                if spell.get_type() == "restoration":
                    # If healing spell is available then choose magic action to try and heal
                    return 1
        else:
            # If health is more than 30 percent, magic should only be used to attack, look for attack spell
            foundAttack = False
            for spell in self.magic:
                if spell.get_type() == "attack":
                    foundAttack = True
            if foundAttack == False:
                # If no attack spell found then choose attack action, not magic action
                return 0
        
        # Otherwise choose an action at random
        return random.randrange(0, 2)

    def choose_magic_ai(self):
        # If health is below 30 percent, look for a healing spell first
        if self.get_hp_percentage() < 30:
            for spell in self.magic:
                if spell.get_type() == "restoration":
                    # If healing spell found, use it
                    return spell
        
        # Choose a spell at random
        spell = self.magic[random.randrange(0, len(self.magic))]

        # Check if chosen spell is appropriate
        if self.mp < spell.cost:
            # If not enough magic points, choose again
            return self.choose_magic_ai()
        if self.get_hp_percentage() > 70 and spell.get_type() != "attack":
            # If health is greater than 70 percent, only use attack spells
            return self.choose_magic_ai()
        else:
            # Return chosen spell
            return spell


    def display_stats(self, enemy=False):
        hp_bar = ""
        hp_bar_ticks = self.get_hp_percentage() / 4
        hp_bar_color = bcolors.OKGREEN
        if enemy:
            hp_bar_color = bcolors.FAIL


        mp_bar = ""
        mp_bar_ticks = self.get_mp_percentage() / 10


        while hp_bar_ticks > 0:
            hp_bar += "█"
            hp_bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        while mp_bar_ticks > 0:
            mp_bar += "█"
            mp_bar_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""

        if len(hp_string) < 12:
            decr = 12 - len(hp_string)
            while decr > 0:
                current_hp += " "
                decr -= 1
            current_hp += hp_string
        else:
            current_hp += hp_string

        mp_string = str(self.mp) + "/" + str(self.maxmp)
        current_mp = ""

        if len(mp_string) < 7:
            decr = 7 - len(mp_string)
            while decr > 0:
                current_mp += " "
                decr -= 1
            current_mp += mp_string
        else:
            current_mp += mp_string

        print("    " + bcolors.BOLD + f'{self.name:15}' +
              current_hp + " |" + hp_bar_color +
              hp_bar +
              bcolors.ENDC + bcolors.BOLD + "| " +
              current_mp + " |" + bcolors.OKBLUE +
              mp_bar + bcolors.ENDC + "|")
    
