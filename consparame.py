class Addition:
    def __init__(self,x,y):
        self.num1=x
        self.num2=y
    def calAdd(self):
        self.add=self.num1+self.num2
        print("Addition :",self.add)


n1=int(input("Enter n1:"))
n2=int(input("Enter n2: "))


A=Addition(n1,n2)
A.calAdd()
