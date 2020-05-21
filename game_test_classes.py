import msvcrt
import time

class Warrior():
    def __init__(self, name):
        self.name = name
        self.max_hp = 120
        self.hp = self.max_hp
        self.atk = 9
        self.dfs = 12
        self.spd = 6
        self.level = 1
        self.experience = 0

        self.damage = 0

    def attack(self, other):
        self.damage = self.atk - other.dfs
        if self.damage >= 0:
            other.hp = other.hp - self.damage
        else:
            self.damage = 0

    def level_up(self):
        if self.experience >= self.level*10:
            self.level += 1
            self.experience = 0
            self.max_hp = self.max_hp * (1 + self.level / 10)
            self.atk = self.atk * (1 + self.level / 10)
            self.dfs = self.dfs * (1 + self.level / 10)
            self.spd = self.spd * (1 + self.level / 10)
            self.hp = self.max_hp

    def get_stats(self):
        print("HP:  " + str(self.hp) +"/" + str(self.max_hp))
        print("ATK: " + str(self.atk))
        print("DEF: " + str(self.dfs))
        print("SPD: " + str(self.spd))


    def get_hp(self):
        print("You are at " + str(self.hp) + "HP")

class Ork():
    def __init__(self, other):
        self.level = int(other.level * 1.1)
        self.max_hp = int(50 * (1 + other.level / 8))
        self.hp = self.max_hp
        self.atk = int(5 * (1 + other.level / 8))
        self.dfs = int(5 * (1 + other.level / 8))
        self.spd = int(5 * (1 + other.level / 8))

        self.damage = 0

    def attack(self, other):
        self.damage = self.atk - other.dfs
        if self.damage >= 0:
            other.hp = other.hp - self.damage
        else:
            self.damage = 0

    def get_stats(self):
        print("HP:  " + str(self.hp) +"/" + str(self.max_hp))
        print("ATK: " + str(self.atk))
        print("DEF: " + str(self.dfs))
        print("SPD: " + str(self.spd))

    def get_hp(self):
        print("The Ork is at " + str(self.hp) + "HP")

def combat(player, entity):
    while player.hp >= 0 or entity.hp >= 0:
        player.attack(entity)
        print("Attack, You did " + str(player.damage) + " Damage!")
        print("Ork is at " + str(entity.hp) + " HP")
        time.sleep(2)
        entity.attack(player)
        print("Ork did " + str(entity.damage) + " Damage!")
        print("You have " + str(entity.hp) + " HP")
        time.sleep(2)
    if player.hp <= 0:
        print("You died")
    elif entity.hp <= 0:
        print("Victory, you did defeat the Ork!")


player_name = input("Hello, please enter your name:\n")
player = Warrior(player_name)
print("Welcome to Warrior vs Orks", player_name)

ork_new = Ork(player)
print("Your stats")
player.get_stats()
time.sleep(5)
print("Ork's stats:")
ork_new.get_stats()
time.sleep(5)
print("Combat is about to beginn")
time.sleep(5)
combat(player, ork_new)


