""" Klasa, która będzie używana do zaprezentowania samochodu """


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
