requested_toppings = ['pieczarki', 'podwójny ser']

if 'pieczarki' in requested_toppings:
    print('Dodaję pieczarki.')
if 'pepperoni' in requested_toppings:
    print('Dodaję pepperoni.')
if 'podwójny ser' in requested_toppings:
    print('Dodaję podwójny ser')

print('Twoja pizza jest już gotowa!')

requested_toppings = ['pieczarki', 'boczek', 'podwójny ser']

for requested_topping in requested_toppings:
    if requested_topping == 'boczek':
        print('Przepraszamy, ale obecnie nie mamy boczku')
    else:
        print('Dodaję ' + requested_topping + "." )

print('\nTwoja pizza jest już gotowa!')
