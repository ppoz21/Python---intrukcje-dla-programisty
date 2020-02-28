import json


def get_stored_username():
    """Pobieranie imienia z pliku, o ile taki istnieje"""
    filename = 'uname.json'

    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """
    Poproszenie użytkownika, aby podał swoje imię,
    a następnie zapisanie tego imienia w pliku.
    """
    username = input("Jak masz na imię?: ")

    filename = 'uname.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """Przywitanie użytkownika jego imieniem."""

    username = get_stored_username()
    if username:
        answ = input("Czy " + username + ' to ty? (tak/nie): ')
        if answ == 'tak':
            print("Witaj ponownie, " + username)
        elif answ == 'nie':
            username = get_new_username()
            print("Twoje imię zostało zapisane i będzie używane póżniej, " +
                  username + '!')
        else:
            print('Błąd!')
            greet_user()
    else:
        username = get_new_username()
        print("Twoje imię zostało zapisane i będzie używane póżniej, " +
              username + '!')


greet_user()
