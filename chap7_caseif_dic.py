def sum1(a, b):
    return a+b
def sub(a, b):
    return a - b

def mul(a , b):
    return a * b

def divide(a , b):
    return a/b

func = [sum1, sub, mul, divide ]
#method one
operator = func[3]
print(operator(1,2))
#method two
print(func[2](12,4))


def dispatch_dict(operator, x ,y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }.get(operator, lambda : None)()

print(dispatch_dict('mul', 2, 8))

print(dispatch_dict('unknown', 2, 8))