def make_sandwich(*toppings):
    print("Przygotowuję kanapkę z:")
    for topping in toppings:
        print('\t- ' + topping)


make_sandwich('ser')
make_sandwich('ser', 'szynka')
make_sandwich('ser', 'keczup', 'pomidor', 'ogórek')
