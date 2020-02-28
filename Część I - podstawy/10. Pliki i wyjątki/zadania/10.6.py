print("Podaj dwie liczby, które mają zostać dodane.")


first_number = input("\nPierwsza liczba: ")

second_number = input("\nDruga liczba: ")

try:
    answer = int(first_number) + int(second_number)
except TypeError:
    print("Podano tekst, zamiast liczby!")
else:
    print(answer)
