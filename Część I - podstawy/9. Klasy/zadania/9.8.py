class User:
    """Profil uzytkownika"""

    def __init__(self, login, f_name, l_name, age, email, phone):
        self.login = login
        self.first_name = f_name.title()
        self.last_name = l_name.title()
        self.age = age
        self.email = email.lower()
        self.phone = phone
        self.login_attempts = 0

    def describe_user(self):
        print('\nUżytkownik o loginie ' + self.login)
        print("--- Dane użytkownika ---")
        print('Imię: ' + self.first_name)
        print('Nazwisko: ' + self.last_name)
        print('Wiek: ' + str(self.age))
        print('Adres e-mail: ' + self.email)
        print('Telefon: ' + self.phone)
        print('--- KONIEC ---\n')

    def greet_user(self):
        print("\nWitaj, " + self.first_name + ' ' + self.last_name + ' (' + self.login
              + ')\n')

    def increment_login_attempts(self, num=1):
        if num > 0:
            self.login_attempts += num
        else:
            print("Błąd, nie można wpisać ujemnej próby logowania")

    def reset_login_attempts(self):
        self.login_attempts = 0


class Privileges:
    """Opis uprawnień"""

    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print('Uprawnienia administratora:')
        for privilege in self.privileges:
            print('\t' + privilege)


class Admin(User):
    """Specjalny rodzaj użytkownika"""

    def __init__(self, login, f_name, l_name, age, email, phone):
        super().__init__(login, f_name, l_name, age, email, phone)
        self.privileges = Privileges(
            ('może dodać post', 'może usunąć post', 'może zbanować użytkownika')
        )


admin = Admin('admin', 'Jan', 'Kowalsky', 25, 'admin@yoursite.pl', '123123123')
admin.privileges.show_privileges()
