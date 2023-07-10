class Base:
    def getdata(self):
        print("This is Base class Function ")

class Derive(Base):
    def getdata(self):
        #super().getdata()
        Base.getdata(self)
        print("This is Derive Class function ")

D=Derive()
D.getdata()
