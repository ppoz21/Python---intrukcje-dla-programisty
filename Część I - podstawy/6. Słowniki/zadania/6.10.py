ulubione_liczby = {
    'janek': [5, 2],
    'janusz': [10, 30],
    'karyna': [69, 96],
    'seba': [2137, 69],
    'grażyna': [2, 4],
}

for k, v in ulubione_liczby.items():
    print(k.title())
    print("Ulubione liczby:")
    for val in v:
        print("\t" + str(val))
    print()
