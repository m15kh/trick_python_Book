class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    def __repr__(self):
        return (f'{self.__class__.__name__}('f'{self.color!r}, {self.mileage!r})')



car1 = Car("red", 1000)
print(car1)