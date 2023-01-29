class Polygon:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    def getArea(self):
        return self.height*self.width
    def getPerimeter(self):
        return 2*(self.height+self.width)