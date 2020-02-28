class Restaurant:
    """Klasa opisująca restaurację"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restauracja " + self.restaurant_name + " serwuje " + self.cuisine_type)


#restaurant = Restaurant('U Janusza', 'schabowe')
#restaurant.describe_restaurant()
