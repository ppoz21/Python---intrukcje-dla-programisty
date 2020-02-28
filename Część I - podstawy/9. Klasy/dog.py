class Dog():
    """Prosta próba modelowania psa"""

    def __init__(self, name, age):
        """Inicjalizacja atrybutów name i age."""
        self.name = name
        self.age = age

    def sit(self):
        """Symulacja, że pies siada po otrzymaniu polecenia."""
        print(self.name.title() + " teraz siedzi.")

    def roll_over(self):
        """Symulacja, że pies kładzie się na plecy po otrzymaniu polecenia."""
        print(self.name.title() + " teraz położył się na plecy.")


my_dog = Dog('szarik', 5)
your_dog = Dog('burek', 6)

print("Mój pies ma na imię " + my_dog.name.title() + '.')
print("Mój pies ma " + str(my_dog.age) + ' lat.')
my_dog.sit()

print("\nTwój pies ma na imię " + your_dog.name.title() + '.')
print("Twój pies ma " + str(your_dog.age) + ' lat.')
your_dog.sit()
