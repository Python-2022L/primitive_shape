from polygon import Polygon
from math import sqrt
class Triangle(Polygon):
    def __init__(self, height, width, uch):
        self.uch = uch
        Polygon.__init__(self, height, width)
    def getArea(self):
        x = (self.width+self.height+self.uch)/2
        return sqrt(x*(x-self.width)*(x-self.height)*(x-self.uch))
    def getPerimeter(self):
        return self.width+self.height+self.uch
a = Triangle(30, 40, 50)
print(a.getArea())
print(a.getPerimeter())