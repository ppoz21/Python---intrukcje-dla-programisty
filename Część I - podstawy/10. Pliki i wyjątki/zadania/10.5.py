filename = 'pool.txt'

answer = ''

while answer != 'q':
    answer = input("Dlaczego lubisz programowanie? (aby zakończyć wpisz 'q'): ")
    if answer != 'q':
        with open(filename, 'a') as file_object:
            file_object.write(answer + '\n')
