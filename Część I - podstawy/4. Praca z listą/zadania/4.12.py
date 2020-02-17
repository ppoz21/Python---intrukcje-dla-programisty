my_foods = ['pizza', 'kebab', 'spagetti']

friend_foods = my_foods[:]

my_foods.append('burger')
friend_foods.append('lody')

print("Moje ulubione potrawy to:")
for food in my_foods:
    print("\t" + food)

print("\nUlubione potrawy mojego przyjaciela to:")
for food in friend_foods:
    print("\t" + food)
