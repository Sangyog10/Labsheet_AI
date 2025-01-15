class Shape:
   
    def area(self):
        return 0
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * (self.radius ** 2)
    
area=Rectangle(10,5).area()
print(f"area of rectangle is {area}")

area=Circle(5)
areaofcircle = area.area()
print(f"area of circle is {areaofcircle}")