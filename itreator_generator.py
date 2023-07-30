class Repeater:
    def __init__(self,value):
        self.value = value
    def __iter__(self):
        return self
    def __next__(self):
        return self.value


#implement above code  with generator



def repeater(value):
    while True:
        yield value


for x in repeater("hi"):
    print(x)