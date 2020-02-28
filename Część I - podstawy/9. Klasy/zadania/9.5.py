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


user = User('j_nosacz', 'janusz', 'nosaczow', 50, 'janusz@NOSACZ.PL', '123456789')
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)
