#%%

import os

os.mkdir('months')
months_list = [f'{str(i).zfill(2)}_raport' for i in range(1, 13)]
print(months_list)

for month in months_list:
    path = os.path.join('months', month) 
    os.mkdir(path)

# %%
    import matplotlib.pyplot as plt



    labels = ['G1', 'G2', 'G3', 'G4', 'G5']
    men_means = [20, 35, 30, 35, 27]
    women_means = [5, 32, 34, 20, 25]
    men_std = [2, 3, 4, 1, 2]
    women_std = [3, 5, 2, 3, 3]
    width = 0.35       # the width of the bars: can also be len(x) sequence

    fig, ax = plt.subplots()

    ax.bar(labels, men_means, width, yerr=men_std, label='Men')
    ax.bar(labels, women_means, width, yerr=women_std, bottom=men_means,
        label='Women')

    ax.set_ylabel('Scores')
    ax.set_title('Scores by group and gender')
    ax.legend()

    plt.show()


# %%
import matplotlib.pyplot as plt

x_values = list(range(1, 101))
y_values = [x ** 2 for x in x_values]

fig, ax = plt.subplots()

ax.plot(x_values, y_values, c='red', linewidth = 3)
ax.set_title('kwadraty liczb', fontsize = 20)
ax.set_xlabel('liczby', fontsize = 16)
ax.set_ylabel('wartości liczby', fontsize = 16)

plt.show()

# %%
