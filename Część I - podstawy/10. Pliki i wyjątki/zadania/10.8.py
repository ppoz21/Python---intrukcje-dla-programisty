def read_file(file):
    try:
        with open(file) as f_obj:
            lines = f_obj.readlines()
    except FileNotFoundError:
        # print("Nie znaleziono pliku " + file)
        pass
    else:
        for line in lines:
            print(line)


files = ['cats.txt', 'dogs.txt']
for file in files:
    read_file(file)