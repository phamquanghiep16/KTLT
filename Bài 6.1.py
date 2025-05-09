print("Phạm Quang Hiệp")
print("MSSV:23575202071001")
print("#####################")
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
radius = float(input("Nhập bán kính của hình tròn: "))
circle = Circle(radius)
print("Diện tích của hình tròn là:", circle.area())

