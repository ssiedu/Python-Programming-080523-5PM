class Base:
    def __init__(self):
        self.r=eval(input("Enter radius of circle :"))


class Derive(Base):
    def calArea(self):
        self.area=3.14*self.r*self.r
    def print(self):
        print("Area of circle :",self.area)



d=Derive()
#d.getdata()
d.calArea()
d.print()

d1=Derive()
#d.getdata()
d1.calArea()
d1.print()
