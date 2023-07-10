class Base:
    def __init__(self):
        self.num1=eval(input("Enter First Number :"))
        self.num2=eval(input("Enter Second Number :"))

class child1(Base):
    def calAdd(self):
        self.add=self.num1+self.num2
        print("Addition :",self.add)

class child2(Base):
    def calMul(self):
        self.mul=self.num1*self.num2
        print("Multiplication :",self.mul)

class child3(Base):
    def calDiv(self):
        self.div=self.num1/self.num2
        print("Division :",self.div)


C1=child1()
C1.calAdd()
C2=child2()
C2.calMul()
C3=child3()
C3.calDiv()





        
