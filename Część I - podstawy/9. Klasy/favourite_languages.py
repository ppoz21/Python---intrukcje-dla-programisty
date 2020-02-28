from collections import OrderedDict

favourite_languages = OrderedDict()

favourite_languages['janek'] = 'python'
favourite_languages['sara'] = 'c'
favourite_languages['edward'] = 'ruby'
favourite_languages['paweł'] = 'python'

for name, language in favourite_languages.items():
    print("Ulubiony język programowania użytkownika " + name.title() +
          " to " + language.title() + '.')