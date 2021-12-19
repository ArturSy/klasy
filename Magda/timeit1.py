#%%

import timeit

numbers = []

print(numbers)

code = """
numbers = []
for i in range(10):
    numbers.append(i)
"""

t_1 = timeit.timeit(code, number = 100000)


code_1 = """

numbers = [x for x in range(10)]


"""

t_2 = timeit.timeit(code_1, number = 1000000)

results = {
    'code' : t_1,
    'code_1' : t_2
}

result = sorted(results.items(), key = lambda x: x[1])[0][0]

print(result)

# %%
