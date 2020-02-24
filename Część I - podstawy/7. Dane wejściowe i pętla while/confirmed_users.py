# Rozpoczynamy od użytkowników, którzy mają być zweryfikowani
# Tworzymy też pustą listę przeznaczoną do przechowywania zweryfikowanych użytkowników

unconfirmed_users = ['alicja', 'bartek', 'katarzyna']
confirmed_users = []

# Weryfikujemy poszczególnych użytkowników, dopóki lista nie będzie pusta.
# Każdego zweryfikowanego użytkownika przenosimy na oddzielną listę

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Weryfikacja użytkownika: " + current_user.title())
    confirmed_users.append(current_user)

# Wyświetlanie wszystkich zweryfikowanych użytkowników
print('\nZweryfikowano poniżej wymienionych użytkowników:')
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
