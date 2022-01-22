#%%


try:
    
    l1 = int(input("podaj 1 liczbe"))
    l2 = int(input("podaj 2 liczbe"))
    print(l1/l2)


except ArithmeticError:
    print("nie dziel cholero przez 0")

except ValueError:
    print("podałeś nie prawidłową wartośc byćmoże literę ")

print("koniec dzialania")

