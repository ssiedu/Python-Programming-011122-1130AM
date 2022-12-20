class Base:
    def getdata(self):
        print("This is Base class Function")

class Derive(Base):
    def getdata(self):
        super().getdata()
        print("This is Derive class function")


d=Derive()
d.getdata()
