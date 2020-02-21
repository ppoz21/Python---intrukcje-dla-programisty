kraje_rzeki = {
    'egipt': 'nil',
    'polska': 'wisła',
    'rosja': 'wołga',
    'anglia': 'tamiza',
    'francja': 'sekwana'
}

for k, v in kraje_rzeki.items():
    print(v.title() + ' przepływa przez ' + k.title())

for rzeka in kraje_rzeki.values():
    print(rzeka.title())

for kraj in kraje_rzeki:
    print(kraj.title())
