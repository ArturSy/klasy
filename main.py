# class mojaKlasa:
#     def wyswietl(x):
#         return 'witaj swiecie'

# x = mojaKlasa()
# print(x.wyswietl())

class prostopadloscian:
    def __init__(self):
        self.podstawa_a = 0
        self.podstawa_b = 0
        self.wysokosc_h = 0
    def objetosc(self):
        return self.podstawa_a * self.podstawa_b * self.wysokosc_h

wtc = prostopadloscian()
wtc.podstawa_a = 100
wtc.podstawa_b = 200
wtc.wysokosc_h = 400

print(wtc.objetosc())