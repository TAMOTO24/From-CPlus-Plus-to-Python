import math

class Triangle:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def getArea(self): # Calculate Area 
        _p = (self.a + self.b + self.c) / 2.0; # Calculate perimeter for Area formul
        return math.sqrt(_p * (_p - self.a) * (_p - self.b) * (_p - self.c))

class Box:
    def __init__(self):
        self.width = 0
        self.height = 0
        self.length = 0
    def __init__(self, x, y, z):
        self.width = x
        self.height = y
        self.length = z
    def getWidth(self):
        return self.width
    def getHeight(self):
        return self.height
    def getLength(self):
        return self.length

    # Class Setters
    def setWidth(self,value):
        self.width = value
    def setHeight(self,value):
        self.height = value
    def setLength(self,value):
        self.length = value
    def Volume(self):
        return self.width * self.height * self.length
    def Compare(self, obj): # Compare two object's
        if self.Volume() < obj.Volume(): print(f"{self.Volume()} is Lower than {obj.Volume()} \n")
        if self.Volume() == obj.Volume(): print(f"{self.Volume()} is equal to {obj.Volume()} \n")
        if self.Volume() > obj.Volume(): print(f"{self.Volume()} is Bigger than {obj.Volume()} \n")

# Class object declaration
a = Triangle(3, 4, 5)
b = Box(2.5, 23.5,12)
c = Box(2.9, 27, 122)

print("Box B.")
print(f"Width: {b.getWidth()}")
print(f"Height: {b.getHeight()}")
print(f"Length: {b.getLength()}")
print(f"Volume: {b.Volume()}\n")

print("Box C.")
print(f"Width: {c.getWidth()}")
print(f"Height: {c.getHeight()}")
print(f"Length: {c.getLength()}")
print(f"Volume: {c.Volume()}\n")
b.Compare(c)
print("Triangle A.")
print(f"Area: {a.getArea()}")