import json

filename = 'favourite_number.txt'

with open(filename, 'w') as f_obj:
    num = input("Wprowadź swoją ulubioną liczbę: ")
    json.dump(num, f_obj)
