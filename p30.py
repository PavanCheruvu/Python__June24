'''
fobj = open('C:\\users\\admin\\emp.csv')
L = fobj.readlines()
fobj.close()
for var in L:
    if('sales' in var):
        eid,ename,edept,ecity,ecost=var.split(',')
        print('{}\t{}'.format(ename,edept))

'''

# print(list(filter(lambda a:'sales' in a,open('C:\\users\\admin\\emp.csv'))))

# print(list(map(lambda a:a.split(','),filter(lambda a:'sales' in a,open('C:\\users\\admin\\emp.csv')))))

print(list(map(lambda a:a.split(',')[1:3],filter(lambda a:'sales' in a,open('C:\\users\\admin\\emp.csv')))))

for v in list(map(lambda a:a.split(',')[1:3],filter(lambda a:'sales' in a,open('C:\\users\\admin\\emp.csv')))):
    print("{}\t{}".format(v[0],v[1]))



