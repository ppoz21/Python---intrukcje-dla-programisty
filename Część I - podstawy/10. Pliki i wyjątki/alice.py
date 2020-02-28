filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Przepraszamy, ale plik " + filename + " nie istnieje."
    print(msg)
else:
    # Obliczanie przybliżonej liczby słów w pliku
    words = contents.split()
    num_words = len(words)
    print("Plik " + filename + " zawiera " + str(num_words) + " słów.")