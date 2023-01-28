class Polygon:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def getArea(self)->int:
        """
        This class returns int
        """
        return self.height * self.width

    def getPerimeter(self)->int:
        """
        this class returns a premeter
        """
        return 2 * (self.height + self.width)

