import random

class Dice:
    def roll(self):
        return random.randint(1, 6)

    def display_roll(self, roll):
        print(f"Dice rolled: {roll}")
