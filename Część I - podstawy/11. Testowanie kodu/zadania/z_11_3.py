class Employee:
    """Klasa opisująca pracownika"""

    def __init__(self, f_name, l_name, salary):
        """Przypisanie danych pracownika"""
        self.first_name = f_name.title()
        self.last_name = l_name.title()
        self.salary = salary

    def give_raise(self, ammount=5000):
        """Zwiększenie pensi pracownika"""
        if ammount > 0:
            self.salary += ammount
        else:
            print("Nie można zwiększyć o ujemną kwotę!")
