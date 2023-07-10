class Base1:
    def getnum1(self):
        self.num1=int(input("Enter first Number :"))


class Base2:
    def getnum2(self):
        self.num2=int(input("Enter second Number :"))

class Base3:
    def getnum3(self):
        self.num3=int(input("Enter third Number :"))
        
class child(Base1,Base2,Base3):
    def cal(self):
        self.p=self.num1*self.num2*self.num3
        print("Product of number :",self.p)


c=child()
c.getnum1()
c.getnum2()
c.getnum3()
c.cal()
