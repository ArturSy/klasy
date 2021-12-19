#%%

import datetime

d_pocz = datetime.date(2019, 1, 1)
d_konc = datetime.date(2021, 8, 9)

wynik = d_konc - d_pocz

print(wynik)
# %%

import datetime

urodziny = datetime.date(1984, 9, 5)
teraz = datetime.date.today()
ilosc_dni = teraz - urodziny

print(ilosc_dni)
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
# %%
