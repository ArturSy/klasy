#%%
def error1(n):
    try:
        return 1/n
    except (ArithmeticError, ValueError, TypeError):
        print("niestety mamy błąd")

    return None

error1("A") 