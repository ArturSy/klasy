#%%

import os

print(os.getcwd())
print(os.listdir())
# %%
import os
filenames = [name for name in os.listdir() if name.startswith('t')] 
print(filenames)
# %%
