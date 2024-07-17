ename = input('Enter an emp name:')
eid = input('Enter {} emp id:'.format(ename))
edept = input(f'Enter {ename} working dept:')

print(f'''Emp name is:{ename}
-------------------------------
{ename} Emp id is:{eid}
-------------------------------
{ename} Working dept is:{edept}
--------------------------------''')
