#%%

import datetime

d_pocz = datetime.date(2019, 1, 1)
d_konc = datetime.date(2021, 8, 9)

wynik = d_konc - d_pocz

print(wynik.days)
# %%

import datetime

urodziny = datetime.date(1984, 9, 5)
teraz = datetime.date.today()
ilosc_dni = teraz - urodziny

print(ilosc_dni.days)
# %%

import datetime 

czas_teraz = datetime.datetime.today()
nowy_rok = datetime.datetime(2021, 12, 31, 23, 59, 59, 999999)
ilosc_dni = nowy_rok - czas_teraz

print(ilosc_dni)



# %%
czas_teraz = datetime.datetime.today()
czas_pozniej = datetime.timedelta(days=31,
minutes=25, hours=30, weeks=7)
print(czas_pozniej)

wynik = czas_teraz + czas_pozniej


print(wynik)

wynik1 = datetime.timedelta(days=7)
wynik2 = datetime.timedelta(days=31)
wynik3 = datetime.timedelta(hours=30)
wynik4 = datetime.timedelta(minutes=25)

print(wynik1,wynik2,wynik3,wynik4)

w1= czas_teraz + wynik1
w2= czas_teraz + wynik2
w3= czas_teraz + wynik3
w4= czas_teraz + wynik4

print(w1)
print(w2)
print(w3)
print(w4)


# %%

# %%
