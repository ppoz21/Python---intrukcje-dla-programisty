pizzas = ['hawajska', 'rzeźnicka', 'margarita']

friends_pizzas = pizzas[:]

friends_pizzas.append('frutti di mare')

print("Moje ulubione rodzaje pizzy to:")
for pizza in pizzas:
    print(pizza)

print("\nUlubione rodzaje pizzy mojego przyjaciela to:")
for pizza in friends_pizzas:
    print(pizza)
