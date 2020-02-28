filename = 'pi_milion_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''

for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + '...')
print(len(pi_string))

birthday = input('Podaj datę urodzenia (w formacie ddmmrr): ')
if birthday in pi_string:
    print("Twoja data urodzenia znajduje się wśród miliona pierwszych cyfr liczby pi!")
else:
    print("Twoja data urodzenia nie znajduje się wśród miliona pierwszych cyfr liczby pi!")
