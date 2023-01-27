class Polygon:
    def __init__(self,heigth,width):
        self.height=heigth
        self.width=width
    def getArea(self):
        """
        This is area

        return --> int
        """
        return self.height*self.width
    def getPerimetr(self):
        """
        This is perimetr

        return --> int
        """
        return 2*(self.height+self.width)
ans=Polygon(10,9)
print(ans.getArea())
print(ans.getPerimetr())