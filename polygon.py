class Polygon:
    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width

    def getArea(self):
        """
        this is Area
        """
        return self.height*self.width
        
    def getPerimeter(self):
        """
        this is Perimeter
        """
        return (self.height+self.width)*2
        
p = Polygon(12,5)
print(p.getArea())
print(p.getPerimeter())