number = int(input("Podaj liczbę, aby dowiedzieć się, czy jest parzysta czy "
                   "nieparzysta: "))

if number % 2 ==0:
    print('\nLiczba ' + str(number) + ' jest parzysta.')
else:
    print('\nLiczba ' + str(number) + ' jest nieparzysta.')
