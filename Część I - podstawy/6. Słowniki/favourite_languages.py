favourite_languages = {
    'janek': 'python',
    'sara': 'c',
    'edward': 'ruby',
    'paweł': 'python',
}

# print('Ulubiony język programowania Sary to ' + favourite_languages['sara'].title() + '.')

for name, language in favourite_languages.items():
    print('Ulubiony jezyk programowania użytkownika ' + name.title() +
          ' to: ' + language.title())
