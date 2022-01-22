slownik = {'a':'b', 'b':'c', 'c':'d'}
ch = 'a'
try:
    while True:
        ch = slownik[ch]
        print(ch)
except KeyError:
    print('nie ma tkaiego klucza', ch)