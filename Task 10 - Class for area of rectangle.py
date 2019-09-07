class Rectangle:
    def __init__(self,length,breadth):
        self.length=length;
        self.breadth=breadth;
    def area(self):
        return self.length*self.breadth;

l = int(input("Enter Length of Rectangle: "));
b = int(input("Enter Breath of Rectangle: "));

obj = Rectangle(l,b);
print("Area Of Rectangle",obj.area());
