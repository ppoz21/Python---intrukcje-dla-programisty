from name_function import get_formatted_name

print("Wpisz 'q', aby zakończyć działanie programu")
while True:
    first = input("Wpisz imię: ")
    if first == 'q':
        break
    last = input("Wpisz nazwisko: ")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)

    print("Sformatowane imię i nazwisko to: " + formatted_name)