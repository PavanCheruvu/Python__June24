class product:
    def f1(self):
        print('F1 block - from parent class')
    def f2(self):
        print('F2 block - from parent class')


class child(product):
    def f3(self):
        print('F3 block')
    def f2(self):
        print('Child block f2')
        super().f2() # python 2.7 updated
        
obj = child()
obj.f1()
obj.f2()
obj.f3()
