"""Zestaw klas przeznaczonych do zaprezentowania samochodu elektrycznego"""

from car import Car


class Battery:
    """Prosta próba modelowania akumulatora samochodu elektrycznego"""

    def __init__(self, battery_size = 70):
        """Inicjalizacja atrybutów akumulatora"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Wyświetlanie informacji o wielkosci akumulatora"""
        print("Ten samochód ma akumulator o pojemności " +
              str(self.battery_size) + " kWh.")

    def get_range(self):
        """
        Wyświetla informacje o zasięgu samochodu na podstawie pojemności
        akumulatora
        """
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "Zasięg tego samochodu wynosi około " + str(range)
        message += " km po pełnym naładowaniu akumulatora."
        print(message)


class ElectricCar(Car):
    """Przedstawia cechy charakterystyczne samochodu elektrycznego"""
    def __init__(self, make, model, year):
        """
        Inicjalizacja atrybutów klasy nadrzędnej
        Następnie inicjalizacja atrybutów charakterystycznych
        dla samochodu elektrycznego
        """
        super().__init__(make, model, year)
        self.battery = Battery()