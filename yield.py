def fun(n):
    for i in range(n):
        yield i


def potega_2(n):
    potega = 1
    for i in range(n):
        yield potega
        potega *=2

for a in potega_2(8):
    print(a)

