current_users = ['admin', 'u1', 'u2', 'u3', 'u4']
new_users = ['U4', 'janusz', 'grażyna', 'ADMIN']

for user in new_users:
    if user.lower() in current_users:
        print('Login zajęty, użyj innej nazwy.')
    else:
        print('Ta nazwa użytkownika jest wolna. ' + user.lower())

