class Area:
    def getradius(self,r):
        self.__r=r
    def calArea(self):
        self.area=3.14*self.__r*self.__r
    def print(self):
        print("area of circle :%.2f"%self.area)

A=Area()
A.getradius(2)
A.calArea()
A.print()
#print("radius :",A.__r)
