responses = {}

while True:
    name = input("\nWprowadź imię: ")
    response = input("Jeżeli mógłbyś odwiedzić jedno dowolne miejsce na świecie, "
                     "gdzie byś pojechał?: ")

    responses[name] = response

    decision = input('\nCzy ktoś jeszcze odpowiada? (tak/nie): ')
    if decision == 'nie':
        break

print('\n--- Wyniki ankiety ---')
for name, response in responses.items():
    print(name + ' chciałby odwiedzić ' + response)