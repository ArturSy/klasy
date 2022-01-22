from math import exp
ex = 1

try:
    while True:
        print(exp(ex))
        ex *=25
except OverflowError:
    print('numer za duży')