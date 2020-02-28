print("Podaj dwie liczby, które mają zostać dodane.")
print("Wpisz 'q', aby zakończyć działanie programu")

while True:
    first_number = input("\nPierwsza liczba: ")
    if first_number == 'q':
        break
    second_number = input("\nDruga liczba: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except TypeError:
        print("Podano tekst, zamiast liczby!")
    else:
        print(answer)
