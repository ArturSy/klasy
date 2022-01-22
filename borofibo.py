class Fib:
    def _init_(self, nn):
        print("Inicjacja.")
        self.__n = nn
        self.__i = 0
        self._p1 = self._p2 = 1

    def _iter_(self):
        print("Iter")
        return self

    def _next_(self):
        print("Next")
        self.__i += 1
        if self._i >self._n:
            raise StopIteration

        if self.__i in[1, 2]:
            return 1

        ret = self._p1 + self._p2
        self._p1, self.p2 = self._p2, ret
        return ret

        
for i in Fib(10):
    print(i)