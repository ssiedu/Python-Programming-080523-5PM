class Base:
    def __init__(self):
        print("This is Base class Function ")

class Derive(Base):
    def __init__(self):
        #super().__init__()
        Base.__init__(self)
        print("This is Derive Class function ")

D=Derive()
