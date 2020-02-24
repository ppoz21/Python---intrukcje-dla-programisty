def make_album(band, title, songs=''):
    """Zwraca album"""
    album = {'band': band, 'title': title}
    if songs:
        album['number_of_songs'] = songs
    return album


while True:
    print("\nProszę podać wykonawcę i tytuł:")
    print("(Wpisz 'q', aby zakończyć pracę w dowolnym momencie)")

    band = input('\tWykonawca: ')
    if band == 'q':
        break
    title = input('\tTytuł: ')
    if title == 'q':
        break

    album = make_album(band, title)
    print(album)
