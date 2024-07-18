print('one')
print('two')
try:
    print(three)
except NameError:
    print('Undefined variable')
else:
    print('the value of three is:',three)
finally:
    print('Thank you')

print('D1')
print('D2')
print('D3')
print('End of the line')
