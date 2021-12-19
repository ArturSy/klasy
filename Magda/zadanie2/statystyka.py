#%%
import statistics

numbers = [1, 5.56, 8.8, 7, 4, 5, 8, 9, 222, 456, 2, 77] 

print(round(statistics.mean(numbers), 2))
print(statistics.median(numbers))
# %%

from statistics import NormalDist

IQ = NormalDist(mu=100, sigma=5)
prob = round(IQ.cdf(104) - IQ.cdf(100), 4)

print(prob)
# %%
