def czytaj_int(prompt, min, max):
    ok = False
    while not ok:
        try:
            wartosc=int(input(prompt))
            ok = True
        except ValueError:
            print('bledna wartosc na wejsciu')
        if ok:
            ok = wartosc>=min and wartosc <=max
        if not ok:
            print("błąd spoza zakresu min/max", min, "a", max)
            wartosc = czytaj_int("wprowadz wartosc spomiedzy zakresu -10 a 10 ", -10,10)
        return wartosc
v= czytaj_int("wprowadz wartosc spomiedzy zakresu -10 a 10 ", -10,10)
print("wybrany numer to: ", v)