def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())


def make_great(names, great_names):
    for name in names:
        name = 'Doskonały ' + name.title()
        great_names.append(name)


mags = ['janusz', 'pjoter', 'somsiad']
great_mags = []
make_great(mags, great_mags)
show_magicians(mags)
show_magicians(great_mags)
