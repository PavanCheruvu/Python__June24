ename = input('Enter an emp name:')

eid = input('Enter an emp ID:')

edept = input('Enter an emp dept:')
'''
print(Emp name is:{}
-------------------------
{} Emp id is:{}
-------------------------
{} Working dept is:{}
--------------------------.format(ename,ename,eid,ename,edept))
'''

print(f'''Emp name is:{ename}
-------------------------------
{ename} Emp id is:{eid}
-------------------------------
{ename} Working dept is:{edept}
--------------------------------''')
