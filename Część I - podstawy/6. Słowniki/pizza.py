# Przechowywanie imformacji o pizzy zamówionej przez klienta
pizza = {
    'crust': 'grubym',
    'toppings': ['pieczarki', 'podwójny ser'],
}
# Podsumowanie zamówienia
print("Zamówiłeś pizze na " + pizza['crust'] + ' cieście' +
      'wraz z następującymi dodatkami:')

for topping in pizza['toppings']:
    print('\t' + topping)