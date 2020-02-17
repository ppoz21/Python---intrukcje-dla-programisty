guests = ['Janusz', 'Grażyna', 'Sebastian']

print(guests[0] + ', zapraszam Cię na flaszkę!')
print(guests[1] + ', zapraszam Cię na flaszkę!')
print(guests[2] + ', zapraszam Cię na flaszkę!')

print(guests[1] + ' nie może przyjść.')
guests[1] = 'Mariusz'

print(guests[0] + ', zapraszam Cię na flaszkę!')
print(guests[1] + ', zapraszam Cię na flaszkę!')
print(guests[2] + ', zapraszam Cię na flaszkę!')

guests.insert(0, 'Mateusz')
guests.insert(1, 'Krystian')
guests.append('Krzysztof')

print(guests[0] + ', zapraszam Cię na flaszkę!')
print(guests[1] + ', zapraszam Cię na flaszkę!')
print(guests[2] + ', zapraszam Cię na flaszkę!')
print(guests[3] + ', zapraszam Cię na flaszkę!')
print(guests[4] + ', zapraszam Cię na flaszkę!')
print(guests[5] + ', zapraszam Cię na flaszkę!')

print('O kurcze, jednak mogę zaprosić tylko 2 osoby')

osoba = guests.pop()
print('Przepraszam, ' + osoba + ", jednak nie możesz przyjść")
osoba = guests.pop()
print('Przepraszam, ' + osoba + ", jednak nie możesz przyjść")
osoba = guests.pop()
print('Przepraszam, ' + osoba + ", jednak nie możesz przyjść")
osoba = guests.pop()
print('Przepraszam, ' + osoba + ", jednak nie możesz przyjść")

print(guests[0] + ', zapraszam Cię na flaszkę!')
print(guests[1] + ', zapraszam Cię na flaszkę!')

del guests[0]
del guests[0]

print(guests)
