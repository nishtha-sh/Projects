import random

class Dice:
    def __init__(self):
        pass

    def roll(self):
        num = random.randint(1,6)
        return num
    

roll1 = Dice()
print(roll1.roll())