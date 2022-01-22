class Stos:
    def __init__(self):
        self.__poziomy = []

    def push(self, data):
        self.__poziomy.append(data)

    def pop(self):
        return self.__poziomy.pop()

stack = Stos()
print(stack.__dict__)

stack.push(55)
stack.push('tak tak')
stack.push('nie nie')
print(stack.pop())
print(stack.pop())
print(stack.pop())

stos1 = Stos()
stos2 = Stos()
stos3 = Stos()

stos1.push(5)
stos2.push(stos1.pop() +1)
stos3.push(stos2.pop() - 2)

print(stos3.pop())
print(stos3.pop())
