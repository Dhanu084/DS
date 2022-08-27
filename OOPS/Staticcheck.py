class Shape:
    shapes = 'shape'

    @staticmethod
    def printShape():
        print(Shape.shapes)

    @property
    def instance(self):
        print(self.printShape())

    def staticToInstance():
        return Shape.instance()
s = Shape()
Shape.printShape()
s.instance
Shape.staticToInstance() 
''' 
throws error as static methods can't access instance methods or variables 
But instance variables can access both static methods and variables
'''