class Simple_Interest:
    def getdata(self):
        self.p=eval(input("Enter principle amount :"))
        self.r=eval(input("Enter rate of interest :"))
        self.t=eval(input("Enter time in year :"))
    def calSI(self):
        self.si=(self.p*self.r*self.t)/100
        print("Simple Interest :",self.si)


s=Simple_Interest()
s.getdata()
s.calSI()
