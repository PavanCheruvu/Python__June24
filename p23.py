'''
def f1(a):
    print('this f1 block')
    return a

rv = f1(10)
print(f'rv value is:{rv}')


def f1(a=150):
    print('this is f1 block')
    n = a+100
    return n

rv1 = f1()
rv2 = f1(10)
print(f'rv1 value is:{rv1}')
print(f'rv2 value is:{rv2}')

def fx():
    return 10,

r = fx()
print(type(r),r)
'''

def display():
    return "STDOUT","STDERR"


r = display()
r1,r2 = r # multiple initialization
print("stdout:",r1)
print("stderr:",r2)





