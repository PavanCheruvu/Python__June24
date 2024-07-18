import sys

print('one')
print('two')
try:
    L=[]
    print(L[1])
except Exception as eobj:
    print('Exception is occured')
    print(sys.exc_info())
else:
    print('the value of three is:',three)
finally:
    print('Thank you')

print('D1')
print('D2')
print('D3')
print('End of the line')
