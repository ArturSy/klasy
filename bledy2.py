#%%
try: 
    skladnik = (input("podaj składnik"))
    zakazane = ("koperek", "kupa", "ananas")

    assert skladnik.lower()not in zakazane

    print(skladnik)
except AssertionError:
    print('nie taki składnik dzbanie')
# %%
