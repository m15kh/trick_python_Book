xs = {'a': 1, 'b': 2}
ys = {'b': 3, 'c': 4}

# Merge xs and ys into zs using the dict() constructor
zs = dict(xs, **ys)
print(zs)  # Output: {'a': 1, 'b': 3, 'c': 4}

xs1 = {'a': 1, 'b': 2}
ys1 = {'b': 3, 'c': 4}

# Merge xs and ys into zs using dictionary unpacking
zs1 = {**xs1, **ys1}
print(zs1)  # Output: {'a': 1, 'b': 3, 'c': 4}
