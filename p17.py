
Fobj = open('E:\\sales.csv','r')
L = Fobj.readlines()
Fobj.close()

for v in L:
    v=v.strip() # remove \n chars
    print(v) # display to monitor

for v in L[-5:]: # last 5 lines
    v=v.strip() # remove \n chars
    print(v) # display to monitor

for v in L[1:6]: # filter 2nd line to 6th line
    v=v.strip() # remove \n chars
    print(v) # display to monitor
