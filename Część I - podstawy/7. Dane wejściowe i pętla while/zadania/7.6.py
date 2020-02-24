# wersja 1

prompt = 'Podaj dodatek do pizzy. (max 3)'
prompt += 'Aby zakończyć, wpisz "koniec"'

counter = 0

while counter < 3:
    dodatek = input(prompt)
    print("Dodałeś " + dodatek)

# wersja 2

prompt = 'Podaj dodatek do pizzy.'
prompt += 'Aby zakończyć, wpisz "koniec"'

active = True

while active:
    dodatek = input(prompt)

    if dodatek.lower() == 'koniec':
        active = False
    else:
        print("Dodałeś " + dodatek)


# wersja 3

prompt = 'Podaj dodatek do pizzy.'
prompt += 'Aby zakończyć, wpisz "koniec"'

while True:
    dodatek = input(prompt)

    if dodatek.lower() == 'koniec':
        break
    else:
        print("Dodałeś " + dodatek)

