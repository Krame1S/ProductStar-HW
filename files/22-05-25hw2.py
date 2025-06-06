class Point:
    def __init__(self, x, y) -> None:
        self._x = x
        self._y = y
    
    def __str__(self):
        return f'Point(x={self._x}, y={self._y})'


#    def __repr__(self):
#        return f'Point(x={self._x}, y={self._y})'

p1 = Point(1,5)
print(p1)
