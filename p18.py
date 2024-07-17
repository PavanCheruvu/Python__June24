
wobj = open('E:\\products.log','a')
 
c = 0
while(c <3):
	pid = input('Enter a product Code:')
	pname = input('Enter a product Name:')
	pCost = input('Enter a product Cost:')
	wobj.write('{}:{}:{}\n'.format(pid,pname,pCost))
	c = c+1
 
wobj.close()

####################################################
wobj = open('E:\\products.log')
s = wobj.read()
print(s)
wobj.close()
