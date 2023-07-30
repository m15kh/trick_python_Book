import  copy
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'Point({self.x!r}, {self.y!r})'

class Rectangle:
    def __init__(self, topleft, bottomright):
        self.topleft = topleft
        self.bottomright = bottomright
    def __repr__(self):
        return (f'Rectangle({self.topleft!r}, '
        f'{self.bottomright!r})')

rect = Rectangle(Point(0, 1), Point(5, 6))
srect = copy.copy(rect)