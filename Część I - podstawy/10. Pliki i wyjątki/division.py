print("Podaj dwie liczby, które mają zostać podzielone.")
print("Wpisz 'q', aby zakończyć działanie programu")

while True:
    first_number = input("\nPierwsza liczba: ")
    if first_number == 'q':
        break
    second_number = input("\nDruga liczba: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("Nie można dzielić przez 0!")
    else:
        print(answer)
