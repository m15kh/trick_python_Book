from json import dumps  as du
mapping = {'a': 23, 'c': 42, 'b': 0xc0ffee}
print(mapping)
x = du(mapping, indent=4, sort_keys=True)#True
print(x)
