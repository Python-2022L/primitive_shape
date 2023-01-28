from polygon import Polygon
class Rectangle(Polygon):
    def __init__(self, height, width):
        super().__init__(height, width)
rect = Rectangle(3, 4)
print(rect.getArea()) # 12
print(rect.getPerimeter()) # 14