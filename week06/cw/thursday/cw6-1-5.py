class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def area(self):
        make_area = self.width * self.height
        print(make_area)

    def perimeter(self):
        make_perimeter = 2 * (self.width+self.height)
        print(make_perimeter)
  
rectangle = Rectangle(20, 12)
rectangle.area()
rectangle.perimeter()
