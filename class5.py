class Largest:
    def getdata(self):
        self.num1=int(input("Enter First Number :"))
        self.num2=int(input("Enter Second Number :"))
    def checknum(self):
        if self.num1>self.num2:
            print(self.num1,"is largest number ")
        else:
            print(self.num2," is largest number ")


L=Largest()
L.getdata()
L.checknum()
