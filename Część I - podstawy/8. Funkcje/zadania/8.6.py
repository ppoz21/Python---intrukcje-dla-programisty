def city_country(city, country):
    """Zwraca stylizowane miasto i kraj"""
    return city.title() + ', ' + country.title()


print(city_country('poznań', 'polska'))
print(city_country('berlin', 'niemcy'))
print(city_country('nowy jork', 'stany zjednoczone'))
