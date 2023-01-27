from polygon import Polygon
class Triangle(Polygon):
    # base classga  geron yozilgan
    def __init__(self, a, b, c):
        super().__init__(a, b, c)
ans=Triangle(4,5,7)
print(ans.getArea())
print(ans.getPerimetr())