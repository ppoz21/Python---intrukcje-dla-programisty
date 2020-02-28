filename = 'guest.txt'

with open(filename, 'w') as file_object:
    name = input("Podaj imię: ")
    file_object.write(name)