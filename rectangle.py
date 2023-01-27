from polygon import Polygon
class Rectangle(Polygon):
    def __init__(self, heigth, width):
        super().__init__(heigth, width)
ans=Rectangle(10,20)
print(ans.getArea())
print(ans.getPerimetr())
