import json

filename = 'favourite_number.txt'

with open(filename) as f_obj:
    print("Znam twoją ulubioną liczbę, to: " + json.load(f_obj))
