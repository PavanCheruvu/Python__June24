for v in open('C:\\users\\admin\\emp.csv'):
    v=v.strip() # remove \n
    eid,ename,edept,ecity,ecost=v.split(',')
    print('{}\t{}\t{}'.format(ename.title(),edept.upper(),ecity.lower()))

