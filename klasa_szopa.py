from klasakot import kot


class szopa:
    def __init__(self, bok_a, bok_b, wys_h):
        self.podstawa_a = bok_a
        self.podstawa_b = bok_b
        self.wysokosc_h = wys_h
    def pomaluj(self):
        return 2 * (self.podstawa_a * self.wysokosc_h) + 2 * (self.podstawa_b * self.wysokosc_h)

szopa1 = szopa(2,3,5)
szopa2 = szopa(5,7,8)


print(szopa1.pomaluj())
print(szopa2.pomaluj())

garfield = kot
garfield.imie = "Garfield"
garfield.wiek = 11
garfield.kolorOczu = 'pomaranczowy'
garfield.waga = 11
garfield.dlugosc = 45

garfield.jedzenie()


print(garfield.waga)
print(garfield.imie)