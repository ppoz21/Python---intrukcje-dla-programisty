def get_formatted_name(first_name, last_name):
    """Zwraca elegancko sformatowane pełne imię i nazwisko"""
    full_name = first_name + last_name
    return full_name.title()


while True:
    print("\nProszę podać imię i nazwisko:")
    print("(Wpisz 'q', aby zakończyć pracę w dowolnym momencie)")

    f_name = input('\tImię: ')
    if f_name == 'q':
        break
    l_name = input('\tNazwisko: ')
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nWitaj, " + formatted_name)
