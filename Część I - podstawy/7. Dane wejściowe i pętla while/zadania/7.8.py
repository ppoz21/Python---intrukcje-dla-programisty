sandwich_orders = ['Big Mac', 'Mc Wrap', 'Big Mac', 'Mc Royal', 'Big Mac',
                   'Kurczakburger', 'Big Mac', 'Drwal']
finished_sandwiches = []

while 'Big Mac' in sandwich_orders:
    sandwich_orders.remove('Big Mac')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("Przygotowano: " + sandwich)
    finished_sandwiches.append(sandwich)

print("Przygotowane kanapki: ")
for sandwich in finished_sandwiches:
    print('\t* ' + sandwich)