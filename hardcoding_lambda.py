#hard coding
a = list(filter(lambda x: x % 2 == 0, range(16)))
print(a)
#clean code
b = [x for x in range(16) if x%2 == 0]
print(b)

#another example

#hard coding

a1 = list(filter(lambda x: x>4, range(10)))
print(a1)


b1 = [x for x in range(10) if x>4]
print(b1)