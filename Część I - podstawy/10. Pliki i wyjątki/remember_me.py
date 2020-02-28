import json

username = input("Jak masz na imię?: ")

filename = 'username.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("Twoje imię zostało zapisane i będzie używane póżniej, " +
          username + '!')
