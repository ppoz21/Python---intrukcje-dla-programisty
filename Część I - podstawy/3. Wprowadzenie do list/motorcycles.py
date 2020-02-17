motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[2] = 'BMW'
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles.insert(0, 'suzuki')
print(motorcycles)

del motorcycles[1]
print(motorcycles)

first_owned = motorcycles.pop(2)
print("Mój pierwszy motocykl to " + first_owned)

motorcycles.remove('ducati')
print(motorcycles)
