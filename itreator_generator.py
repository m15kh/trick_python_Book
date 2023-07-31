def integers():
    for i in range(1, 9):
        yield i
chain = integers()

def squared(seq):
    for i in seq:
        yield i * i

chain2 = squared(integers())
print(list(chain2))

def negated(seq):
    for i in seq:
        yield -i

chain3 = negated(squared(integers()))
print(list(chain3))
