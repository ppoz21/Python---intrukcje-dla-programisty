languages = {
    'python': 'Dobry język',
    'c++': 'fujka',
    'php': '"Ale ten język jest zajebisty" - M.S.',
    'c#': 'Adam M. lubi to!'
}

for language in languages:
    if language == 'php':
        print(language.upper() + ': ' + languages[language])
    else:
        print(language.title() + ': ' + languages[language])
