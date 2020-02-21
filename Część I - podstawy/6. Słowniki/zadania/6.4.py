languages = {
    'python': 'Dobry język',
    'c++': 'fujka',
    'php': '"Ale ten język jest zajebisty" - M.S.',
    'c#': 'Adam M. lubi to!'
}

for key, value in languages.items():
    if key == 'php':
        print(key.upper() + ': ' + value)
    else:
        print(key.title() + ': ' + value)
