class fibo:
    def __init__(self, nn):
        print("inicjujemy")
        self.__n=nn
        self.__i=0
        self.__p1=self.__p2=1
    
    def __iter__(self):
        print("iter")
        return self

    def __next__(self):
        print("next")
        self.__i+=1
        if self.__i>self.__n:
            raise StopIteration
        if self.__i in[1,2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret


for i in fibo(10):
    print(i)