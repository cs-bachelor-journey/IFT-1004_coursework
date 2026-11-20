from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = 2 * radius
    
    def area(self):
        return self.radius * self.radius * pi 
    
    def circonference(self):
        return self.diameter * pi
    
    def multiply_radius(self, bill):
        self.radius = self.radius * bill
        self.diameter = 2 * self.radius
        
    def display(self):
        print("The rdius of the circle is: ", self.radius)

if __name__ == "__main__":
    c_1 = Circle(5)
    c_2 = Circle(10)
    print(type(c_1))
    print(c_1.area(), c_2.area())