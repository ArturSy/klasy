class Zwierze:
    def _init_(self,nazwa,wiek,waga):
        self.nazwa = nazwa
        self.waga = waga
        self.wiek = wiek

    def podaj_dane(self):
        print(f'jestem zwierzęciem {self.nazwa}, mam {self.wiek} lat i ważę {self.waga} kg.')


class Slon(Zwierze):
    pass

class Lew(Zwierze):
    def __init__(self):
        self.iloscKlow = 4

Dumbo = Slon()
Dumbo.nazwa = 'Slonik Dumbo'
Dumbo.waga = 300
Dumbo.wiek = 400

Simba = Lew()
Simba.iloscKlow = 3
Simba.wiek = 34
Simba.nazwa = 'Lew Simba'
Simba.waga = 450

class Papuga(Zwierze):
    def __init__(self, nazwa, dlg_skrzydel):
        self.iloscPior = 4000
        self.nazwa = nazwa
        self.dlg_skrzydel = dlg_skrzydel

class Hybryda(Lew, Papuga)
    pass

hyb = Hybryda()
hyb.


Simba.podaj_dane()
Dumbo.podaj_dane()
