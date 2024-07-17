
L=['Raj,sales,pune,1000\n','Leo,prod,bglore,2000\n','Rya,HR,Hyd,3000\n']

total = 0
for v in L:
    v=v.strip() # remove \n 
    en,ed,ec,ecost = v.split(",") # multiple initialization
    print(f'Emp name:{en} Working City:{ec}')
    total = total + int(ecost)

print(f"Sum of Emp's Cost:{total}")

