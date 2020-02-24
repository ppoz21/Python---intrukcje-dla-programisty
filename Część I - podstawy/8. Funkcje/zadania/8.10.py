def show_magicians(magicians):
    for magician in magicians:
        print(make_great(magician.title()))


def make_great(name):
    return 'Doskonały ' + name


mags = ['janusz', 'pjoter', 'somsiad']
show_magicians(mags)
