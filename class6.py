class Number:
    def getnum(self):
        self.num=int(input("Enter any number :"))
    def printseries(self):
        for i in range(self.num+1):
            print(i,end=" ")


n=Number()
n.getnum()
n.printseries()
