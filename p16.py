
Fobj = open("E:\\sales.csv","r") # open an existing file

s = Fobj.read() # read a content

Fobj.close()  # close a file

print(s) # display file content to monitor

print('') # empty line

Fobj = open('E:\\sales.csv','r')
L = Fobj.readlines()
Fobj.close()

print(L[-3:]) # display last 3 lines
