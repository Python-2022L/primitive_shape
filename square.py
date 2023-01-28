from polygon import Polygon
class square (Polygon):
    def __init__(self,height):
        self.height = height
        

kvadrat = Polygon(8,8)
print(kvadrat.getArea())
print(kvadrat.getPerimeter())