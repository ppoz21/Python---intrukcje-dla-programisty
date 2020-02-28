class Die:
    """Klasa symulująca rzut kostką"""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        from random import randint
        print(randint(1, self.sides))


kostka_6_scian = Die()
print("Rzuty 6-ścienną kostką:")
for i in range(1, 11):
    kostka_6_scian.roll_die()

kostka_10_scianek = Die(10)
print("\nRzuty 10-ścienną kostką:")
for i in range(1, 11):
    kostka_10_scianek.roll_die()

kostka_20_scianek = Die(20)
print("\nRzuty 20-ścienną kostką:")
for i in range(1, 11):
    kostka_20_scianek.roll_die()
