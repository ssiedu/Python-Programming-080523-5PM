class Base:
    def __init__(self):
        self.l=eval(input("Enter length of rectangle:"))
        self.b=eval(input("Enter breadth of rectangle :"))


class Parent1(Base):
    def calArea(self):
        self.Rect_area=self.l*self.b


class Parent2:
    def getRadius(self):
        self.r=eval(input("Enter Radius of circle :"))
    def calCArea(self):
        self.Cir_area=3.14*self.r*self.r


class child(Parent1,Parent2):
    def display(self):
        print("Area of rectangle :", self.Rect_area)
        print("Area of Circle :", self.Cir_area)


c=child()
c.calArea()
c.getRadius()
c.calCArea()
c.display()





        
