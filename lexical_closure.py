def adder(x):
    def add(y):
        return x + y
    return add

a1 = adder(3)
print(a1(13))

class adder_class():
    def __init__(self, x):
        self.x = x
    def __call__(self, y):
        return self.x + y

a2 = adder_class(4)
print(a2(3))


def add_lam(n):
    return lambda x :x + n
a3 = add_lam(34)
print(a3(12))