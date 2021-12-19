#%%

import collections

city1 = {'yes' : 250, 'no' : 138, None: 17}
city2 = {'yes' : 193, 'no' : 232, None: 19}

glosy1 = collections.Counter(city1)
glosy2 = collections.Counter(city2)

razem = glosy1 + glosy2

print(razem)

city3 = {'yes' : 111, 'no' : 111, None: 111}
glosy3 = collections.Counter(city3)

razem1 = razem + glosy3

print(razem1)
print(razem1['yes'])
# %%
import collections

nazw = "Artur Sybila"
print(collections.Counter(nazw.replace(" ", "").lower()))
# %%
