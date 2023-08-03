xs = {'a': 4, 'c': 2, 'b': 3, 'd': 1}

s = sorted(xs.items(), key=lambda x: x[0])
print(s)