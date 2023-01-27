from polygon import Polygon

class Rectangle(Polygon):
    def __init__(self, height, width) -> None:
        super().__init__(height, width)

r = Rectangle(2,3)
print(r.getArea())