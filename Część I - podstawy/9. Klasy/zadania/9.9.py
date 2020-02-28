class Car:
    """Prosta próba zaprezentowania samochodu"""

    def __init__(self, make, model, year):
        """Inicjalizacja atrybutów opisujacych samochód"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Zwrot elegancko sformatowanego tekstu"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Wyświetla informację o przebiegu samochodu"""
        print("Ten samochód ma przejechane " + str(self.odometer_reading)
              + " km.")

    def update_odometer(self, milage):
        """
        Przypisanie podanej wartości licznikowi przebiegu samochodu.
        Zmiana zostanie odrzucona w przypadku próby cofnięcia licznika.
        """
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("Nie można cofnąć licznika przebiegu samochodu!")

    def increment_odometer(self, kilometers):
        """Inkrementacja wartości licznika przebiegu samochodu o podaną wartość"""
        if kilometers >= 0:
            self.odometer_reading += kilometers
        else:
            print("Nie można cofnąć licznika przebiegu samochodu!")


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

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85


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


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
