class Parent:
    def __init__(self,a,b):
        print('Parent Block - constructor')
        self.a = a
        self.b = b

class Child(Parent):
    def __init__(self,a,b):
        self.a = a+100
        self.b = b+100
        super().__init__(self.a,self.b) # calling parent clas constructor
    def fx(self):
        return self.a,self.b

obj = Child(10,20)
r = obj.fx()
print(r)
