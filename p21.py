Fobj = open('C:\\users\\Admin\\emp.csv','r')

L = Fobj.readlines()

Fobj.close()

total = 0

for v in L:
    v=v.strip()
    if('sales' in v):
        eid,ename,edept,ecity,ecost=v.split(",")
        print(f"Emp name:{ename} City:{ecity}")
        total = total + int(ecost)

print(f"Sum of sales emp cost:{total}")
