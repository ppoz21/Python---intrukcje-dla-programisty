favourite_places = {
    'janusz': ['kanapa', 'fotel', 'dom kochanki'],
    'grażyna': ['biedronka', 'kuchnia', 'łóżko janusza'],
    'pjoter': ['boisko', 'gdziekolwiek na papierosku', 'łóżko dżesiczki']
}

for k, v in favourite_places.items():
    print(k.title() + ':')
    for val in v:
        print("\t" + val)
