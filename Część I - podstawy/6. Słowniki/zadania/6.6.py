favourite_languages = {
    'janek': 'python',
    'sara': 'c',
    'edward': 'ruby',
    'paweł': 'python',
}

osoby = ['janek', 'franek', 'alicja', 'sara', 'kinga', 'edward', 'piotr', 'paweł']

for osoba in sorted(osoby):
    if osoba in favourite_languages.keys():
        print(osoba.title() + ", dziękujemy za udział w ankiecie!")
    else:
        print(osoba.title() + ', zapraszamy do udziału w ankiecie!')
