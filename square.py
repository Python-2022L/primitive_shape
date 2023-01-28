from polygon import Polygon
class Square(Polygon):
    def __init__(self, height):
        super().__init__(height, height)

sq = Square(5)
print(sq.getArea()) # 25
print(sq.getPerimeter()) # 20