#hardcoding
a = list(filter(lambda x: x % 2 == 0, range(16)))
print(a)
#clean code
b= [x for x in range(16) if x%2 == 0]
print(b)