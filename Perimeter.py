import math

class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
    def perimeter(self):
        return 2 * math.pi * self.radius
user_radius = float(input("Enter the radius of the circle: "))
circle = circle(user_radius)

print("The area of the circle is:", circle.area())
print("The perimeter of the circle is:", circle.perimeter())
