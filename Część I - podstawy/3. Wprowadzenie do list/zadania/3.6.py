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
