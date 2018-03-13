from random import randint

class Dice():
    """Class to  describe a dice and it behaviour"""

    def __init__(self, sides=6):
        """Initialization of the value of the dice"""
        self.sides = sides

    def roll_dices(self):
        """Print a random value of a dice"""
        x = randint(1, self.sides)
        print(x)

dice_1 = Dice(10)
dice_1.roll_dices()
dice_1.roll_dices()
dice_1.roll_dices()
