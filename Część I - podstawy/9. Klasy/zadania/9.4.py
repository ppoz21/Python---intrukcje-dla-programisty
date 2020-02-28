class Restaurant:
    """Klasa opisująca restaurację"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("Restauracja " + self.restaurant_name + " serwuje " + self.cuisine_type)

    def display_number_served(self):
        print("Restauracja obsłużyła dzisiaj " + str(self.number_served) + " klientów.")

    def set_number_served(self, number):
        if number >= self.number_served:
            self.number_served = number
        else:
            print("Nie można przypisać mniejszej liczby klientów, niż poprzednia!")

    def increment_number_served(self, number):
        if number >= 0:
            self.number_served += number
        else:
            print("Nie można przypisać ujemnych klientów!")


restaurant = Restaurant('U Janusza', 'schabowe')
restaurant.describe_restaurant()
restaurant.display_number_served()
restaurant.set_number_served(100)
restaurant.display_number_served()
restaurant.set_number_served(50)
restaurant.display_number_served()
restaurant.increment_number_served(50)
restaurant.display_number_served()
restaurant.increment_number_served(-70)
restaurant.display_number_served()
