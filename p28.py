'''
def f1(a):
	return a.title()
    f1('abc')
'''

f1 = lambda a:a.title()
print(f1('abc'))
print(f1('python'))

'''
  def f2(a1,a2):
	return a1+a2*5
  
'''
f2 = lambda a1,a2:a1+a2*5
print(f2(10,20))
print(f2(1.45,0.03))
'''
   def f3(a1,a2):
	return a1 >a2
'''
f3 = lambda a1,a2:a1 >a2
print(f3(150,230))
print(f3(123,56))
