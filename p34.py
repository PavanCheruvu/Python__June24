import sys

print('one')
print('two')
try:
    fobj = open('E:\\test1.csv')
except Exception as eobj:
    print('Exception is occured')
    print(sys.exc_info())
else:
    for var in fobj:
        print(var.strip())
finally:
    print('Thank you')

print('D1')
print('D2')
print('D3')
print('End of the line')
