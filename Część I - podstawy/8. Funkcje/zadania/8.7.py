def make_album(title, band, songs=''):
    """Zwraca album"""
    album = {'band': band, 'title': title}
    if songs:
        album['number_of_songs'] = songs
    return album


print(make_album('marmur', 'taco hemingway'))
print(make_album('umowa o dzieło', 'taco hemingway', 8))
