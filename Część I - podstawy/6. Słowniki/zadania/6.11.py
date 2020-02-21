cities = {
    'poznań': {
        'populacja': '537 682',
        'powieżchnia': '261.91 km^2',
        'województwo': 'wielkopolskie',
    },
    'warszawa': {
        'populacja': '1 777 972',
        'powieżchnia': 	'517.24 km^2',
        'województwo': 'mazowieckie',
    },
    'kraków': {
        'populacja': '774 839',
        'powieżchnia': 	'326.85 km^2',
        'województwo': 'małopolskie',
    },
    'wrocław': {
        'populacja': '641 607',
        'powieżchnia': 	'292.82 km^2',
        'województwo': 'dolnośląskie',
    }
}

for k, v in cities.items():
    print(k.title() + ":")
    for k2, v2 in v.items():
        print("\t" + k2.title() + ": " + str(v2))
