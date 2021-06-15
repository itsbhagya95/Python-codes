class Test:
    def __init__(self):
        self.a=10
        self.b=20
    def m1(self):
        self.c=30
t=Test() ##adds a,b to the instance object
t.m1() ##adds c to the instance object
t.d=40 ##adds d to the instance object
print(t.__dict__)
