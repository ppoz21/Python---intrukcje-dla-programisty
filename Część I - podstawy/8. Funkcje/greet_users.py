def gret_users(names):
    """Wyświetla proste powitanie każdemu użytkownikowi z listy"""
    for name in names:
        msg = "Witaj, " + name.title() + "!"
        print(msg)


usernames = ['janusz', 'grażyna', 'pjoter', 'dżesika']
gret_users(usernames)
