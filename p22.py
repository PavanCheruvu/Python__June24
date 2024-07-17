d={} # empty dict

Fobj = open("C:\\users\\admin\\network.conf") # open an existing conf file
L = Fobj.readlines() # read a entire file content and initialize to list
Fobj.close()

for v in L: # iterate a list
    v=v.strip() # remove \n chars
    K,V = v.split("=") # split single value to mutliple initialization
    d[K]= V # adding new data to an existing dict

for var in d:   # display key - value details
    print("{} {}".format(var,d[var])) # d.get(var)
    

d['bootproto']='static'  # dict modification
d['defroute']='no'       # dict modification
d['IPADDR']='10.20.30.40' # dict - adding new data
d['PREFIX']=24            # dict - adding new data

print('\nUpdated dict details:-')
for var in d:
    print("{} {}".format(var,d[var])) # d.get(var)

with open('E:\\newnetwork.conf','w') as wobj:   # create a new config file and write updated
    for var in d:                               # dict content to file
        wobj.write("{}={}\n".format(var,d[var]))

