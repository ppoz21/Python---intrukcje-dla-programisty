class User:
    """Profil uzytkownika"""

    def __init__(self, login, f_name, l_name, age, email, phone):
        self.login = login
        self.first_name = f_name.title()
        self.last_name = l_name.title()
        self.age = age
        self.email = email.lower()
        self.phone = phone

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


user1 = User('j_nosacz', 'janusz', 'nosacz', 56, 'janusz@NOSACZ.PL', '123456789')
user2 = User('grazka', 'grażyna', 'nosaczowa', 50, 'GRAŻKA@nosacz.pl', '234567890')
user3 = User('pjoter', 'pjoter', 'nosacz', 16, 'ruchacz123@porn.com', '345678901')

user1.describe_user()
user2.describe_user()
user3.describe_user()

user1.greet_user()
user2.greet_user()
user3.greet_user()
