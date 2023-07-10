class Addition:
    def getdata(self):
        self.num1=int(input("Enter first Number :"))
        self.num2=int(input("Enter Second Number :"))
    def calculate(self):
        self.add=self.num1+self.num2
    def display(self):
        print("Addition :",self.add)


a=Addition()
a.getdata()
a.calculate()
a.display()
b=Addition()
b.getdata()
b.calculate()
b.display()
