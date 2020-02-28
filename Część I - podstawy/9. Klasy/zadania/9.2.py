class Restaurant:
    """Klasa opisująca restaurację"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restauracja " + self.restaurant_name + " serwuje " + self.cuisine_type)


restaurant1 = Restaurant('U Janusza', 'schabowe')
restaurant1.describe_restaurant()

restaurant2 = Restaurant('U grażyny', 'pierogi')
restaurant2.describe_restaurant()

restaurant3 = Restaurant('u pjotera', 'narkotyki')
restaurant3.describe_restaurant()
