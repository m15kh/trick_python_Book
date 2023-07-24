def cheaker(func):
    def wrapper(x, y):
        if y == 0:
            return print("error zeroo division :(((")
        else:
            return func(x, y)
    return wrapper
@cheaker
def divider(x , y):
    print(x/y)

divider(2,0)