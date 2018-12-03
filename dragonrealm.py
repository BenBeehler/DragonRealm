import random
import os

class Item:
    attack = 0
    def __init__(self, name, attack):
        self.attack = attack


class Character:
    #character class handles name, data, health, and backpack
    name = ""
    items = []
    money = 0
    health = 100

    def __init__(self, name):
        self.name = name
        

class Dungeon:
    iterations = 0
    actions = []
    current_enemy = None

    def __init__(self, iterations):
        self.iterations = iterations


class Map:
    character = Character("Player")

    def __init__(self):
        self.character.name = input("What would you like to be called? ")
        print("Welcome, " + self.character.name + ", to Dragon Realm. A new procedural world is now being generated...")

#Program entry
os.system("START music.mp3")

map = Map()


