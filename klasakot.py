class kot:
    def __init__(self):
        self.imie = ''
        self.kolorOczu = ''
        self.kolorSiersci = ''
        self.dlugosc = 0
        self.wysokosc = 0
        self.wiek = 0
        self.waga = 1
    def miauczenie(self):
        return "miauuuu"
    def jedzenie(self):
        self.waga += 10
        print(self.waga)
        print('kot dobrze zjadł')
    def spanie(self):
        if self.wiek <=10:
            print("spi godzinke")
        elif self.wiek > 10:
            print("spi 3 godziny")
    def drapanie(self):
        if self.waga > 10:
            return 'spore zniszczenia'
    def mruczenie(self):
        return "mrrrrrrrr"
    




#miauczenie jedzenie spanie drapanie mruczenie