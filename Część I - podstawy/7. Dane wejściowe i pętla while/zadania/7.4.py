prompt = 'Podaj dodatek do pizzy.'
prompt += 'Aby zakończyć, wpisz "koniec"'

while True:
    dodatek = input(prompt)

    if dodatek.lower() == 'koniec':
        break
    else:
        print("Dodałeś " + dodatek)
