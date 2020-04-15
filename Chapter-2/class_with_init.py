class Point:
    def __init__(self, x, y):
        self.move(x,y)

    def move(self, x, y):
        self.x = x
        self.y = y
        
#Constructing a Point
point = Point(3, 7)
print(point.x, point.y)