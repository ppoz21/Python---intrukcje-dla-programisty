import json


def get_new_number():
    num = input("Podaj swoją ulubioną liczbę: ")
    filename = 'favourite_number.txt'
    with open(filename, 'w') as f_obj:
        json.dump(num, f_obj)
    return num


def get_stored_number():
    filename = 'favourite_number.txt'
    try:
        with open(filename) as f_obj:
            num = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return num


def favourite_number():
    number = get_stored_number()
    if number:
        print("Znam twoją ulubioną liczbę, to: " + number)
    else:
        number = get_new_number()
        print("Twoja liczba została zapisana: " + number)


favourite_number()
