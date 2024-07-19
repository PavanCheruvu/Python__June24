class Enrollment:
    __name = ''
    __dob = ''
    __place = ''
    def f1(self,n,d,p='CityA'):
        self.__name = n
        self.__dob = d
        self.__place = p
        print('Enrollment is done')
    def f2(self):
        print(f'Emp name:{self.__name} DOB:{self.__dob} Place:{self.__place}')


obj1 = Enrollment()
obj1.f1('Arun','1st Jan','City-1')
                                 
obj2 = Enrollment()
obj2.f1('Rya','2nd Feb','City-2')

obj3 = Enrollment()
obj3.f1('Leo','3rd March','City-3')

for var in [obj1,obj2,obj3]:
    var.f2()
    print('') # empty line



    
