class Parent:
    def __init__(self,a,b):
        print('Parent Block - constructor')
        self.a = a
        self.b = b

class Child(Parent):
    def fx(self):
        return self.a,self.b

obj = Child(10,20)
r = obj.fx()
print(r)



