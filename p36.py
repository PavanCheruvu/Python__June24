class Enrollment:
    name = ''
    dob = ''
    place = ''

obj1 = Enrollment()
obj1.name = 'Arun'
obj1.dob = '1st Jan'
obj1.place = 'City-1'

obj2 = Enrollment()
obj2.name = 'Rya'
obj2.dob = '2nd Feb'
obj2.place = 'City-2'

print(f'Emp name:{obj1.name} DOB:{obj1.dob} Place:{obj1.place}')
print(f'Emp name:{obj2.name} DOB:{obj2.dob} Place:{obj2.place}')
