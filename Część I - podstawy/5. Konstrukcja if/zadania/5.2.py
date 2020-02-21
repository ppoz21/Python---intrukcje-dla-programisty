tekst1 = 'python'
tekst2 = 'PYTHON'
tekst3 = 'PyThOn'

if tekst1 == tekst2:
    print('tekst1==tekst2')
else:
    print('tekst1!=tekst2')

if tekst1.lower() == tekst2.lower():
    print("tekst1.lower() == tekst2.lower()")
else:
    print("tekst1.lower() != tekst2.lower()")

age = 17

if age >= 18:
    print('Browar')
else:
    print('Soczek')

if tekst1.lower() == tekst2.lower() and tekst2.lower() == tekst3.lower():
    print('tekst1.lower() == tekst3.lower()')
