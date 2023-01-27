from polygon import Polygon
class Square(Polygon):
    def __init__(self, heigth):
        self.height=heigth
ans=Polygon(10,10)
print(ans.getArea())
print(ans.getPerimetr())