class Rect:
    def getdata(self):
        self.l=2
        self.b=3
    def calArea(self):
        self.area=self.l*self.b
        print("Area of rectangle :",self.area)


R=Rect()
R.getdata()
R.calArea()
