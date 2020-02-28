filename = 'guest_book.txt'

name = ''

while name != 'q':
    name = input("Wpisz imię (aby zakończyć wpisz 'q'): ")
    if name != 'q':
        with open(filename, 'a') as file_object:
            file_object.write(name + '\n')
