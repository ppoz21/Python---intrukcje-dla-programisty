prompt = "Podaj wiek: "

while True:
    wiek = int(input(prompt))

    if wiek < 3:
        cena = 0
    elif wiek <= 12:
        cena = 10
    else:
        cena = 15

    cont = input("Jeżeli chcesz zakończyć, wpisz 'koniec'")
    if cont == 'koniec':
        break
