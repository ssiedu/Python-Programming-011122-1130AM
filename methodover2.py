class Demo:
    def __init__(self):
        print("This is Demo class")

class derive(Demo):
    def __init__(self):
        super().__init__()
        print("This is derive class")

d=derive()
