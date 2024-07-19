class Enrollment:
    name = ''
    dob = ''
    place = ''
    def f1(self,n,d,p='CityA'):
        self.name = n
        self.dob = d
        self.place = p
        print('Enrollment is done')
    def f2(self):
        print(f'Emp name:{self.name} DOB:{self.dob} Place:{self.place}')

##########################################################################
obj1 = Enrollment()
obj1.f1('Arun','1st Jan','City-1')

obj2 = Enrollment()
obj2.f1('Rya','2nd Feb','City-2')

obj3 = Enrollment()
obj3.f1('Leo','3rd March','City-3')

for var in [obj1,obj2,obj3]:
    var.f2()
    print('') # empty line
