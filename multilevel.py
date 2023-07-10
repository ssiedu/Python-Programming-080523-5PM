class simple_interest:
    def __init__(self):
        self.p=eval(input("Enter principle amount :"))
        self.r=eval(input("Enter rate of interest :"))
        self.t=eval(input("Enter time in year :"))
        
class Parent(simple_interest):
    def calculate(self):
        self.si=(self.p*self.r*self.t)/100
        self.total=self.p+self.si


class child(Parent):
    def display(self):
        print("Simple Interest :",self.si)
        print("Total Amount :",self.total)


C1=child()
C1.calculate()
C1.display()
