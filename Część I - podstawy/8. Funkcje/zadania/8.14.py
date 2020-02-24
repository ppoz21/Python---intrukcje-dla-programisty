def make_car(brand, model, **kwargs):
    car = {
        'brand': brand,
        'model': model,
    }
    for key, value in kwargs.items():
        car[key] = value

    return car


car = make_car('bmw', '318i',
               color='stahlgrau metallic',
               tow_paskage=False,
               engine='2.0',
               fuel='petrol')

print(car)
