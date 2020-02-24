def describe_pet(pet_name, animal_type='pies'):
    """Wyświetla informacje o zwierzęciu"""
    print("\nMoje zwierzę to " + animal_type + ".")
    print("Mój " + animal_type + " ma na imię " + pet_name.title() + ".")


describe_pet('harry', 'chomik')
describe_pet(animal_type='pies', pet_name='larry')
describe_pet('janusz')
