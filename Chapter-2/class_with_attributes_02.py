import math

class Point:
    def move(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        self.move(0,0)

    def calculate_distance(self, other_point):
        return math.sqrt(
            (self.x - other_point.x)**2 +
            (self.y - other_point.y)**2
        )

point1 = Point()
point2 = Point()

point1.move(2,3)
point2.move(7,8)
print(point1.calculate_distance(point2))