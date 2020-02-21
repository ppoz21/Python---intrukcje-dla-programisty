username = 'admin'
users = []

if username == 'admin':
    print('Witaj Administratorze, czy chcesz przejrzeć dzisiejszy raport?')
    if not users:
        print('Musimy znaleść jakichś użytkowników!')
else:
    print('Witaj ' + username + '! Dziękujemy, że ponownie się zalogowałeś.')