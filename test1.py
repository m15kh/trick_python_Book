



from time import perf_counter
from functools import wraps
def dec(func):
    @wraps (func)
    def inner (*args, **kwargs):
        #time before run a func
        before = perf_counter()
        value = func(*args, **kwargs)
        #time after run a func
        after = perf_counter()
        pichidegi =  after - before
        print (f"pichidegi zamani ", func.__name__, pichidegi)
        return None
    return inner
l = [1, 3, 5, 6, 9]
@dec
def moraba_2(l):
    print([x**2 for x in l])

@dec
def moraba_1(l):
    print([x**2 for x in l])

moraba_1(l)
moraba_2(l)


