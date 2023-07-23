def my_decorators(func):
    def wrapper(x, y):
        if y == 0:
            return print(("what the fuck zero error"))
        else:
            return func(x,y)

    return wrapper
@my_decorators
def divide(x,y):
    print(x/y)

divide(1,)

