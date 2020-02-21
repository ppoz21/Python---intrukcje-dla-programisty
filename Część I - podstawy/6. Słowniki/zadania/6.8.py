pies = {
    'gatunek': 'pies',
    'własciciel': 'janusz',
    'imię': 'burek',
    'wiek': 10,
}
kot = {
    'gatunek': 'kot',
    'własciciel': 'grażyna',
    'imię': 'kicia',
    'wiek': 2
}
chomik = {
    'gatunek': 'chomik',
    'własciciel': 'pioter',
    'imię': 'śmierdziel',
    'wiek': 1
}

pets = [pies, kot, chomik]

for pet in pets:
    for key, value in pet.items():
        print(key.title() + ': ' + str(value).title())
    print()
