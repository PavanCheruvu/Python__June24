import pprint

def f1():
    d={}
    return d


def f2(d):
    Fobj = open("C:\\users\\admin\\network.conf") # open an existing conf fil
    L = Fobj.readlines() # read a entire file content and initialize to list
    Fobj.close()
    for v in L: # iterate a list
        v=v.strip() # remove \n chars
        K,V = v.split("=") # split single value to mutliple initialization
        d[K]= V # adding new data to an existing dict

    return d

def f3(d):
    for var in d:   # display key - value details
        print("{} {}".format(var,d[var])) # d.get(var)

def f4(d):
    d['bootproto']='static'  # dict modification
    d['defroute']='no'       # dict modification
    d['IPADDR']='10.20.30.40' # dict - adding new data
    d['PREFIX']=24            # dict - adding new data
    return d

def f5(d):
    with open('E:\\newnetwork.conf','w') as wobj:   # create a new config file and write updated
        for var in d:                               # dict content to file
            wobj.write("{}={}\n".format(var,d[var]))

    

rv1 = f1()
rv2 = f2(rv1)
f3(rv2)
rv3 = f4(rv2)
print("Updated dict details:")
#pprint.pprint(rv3)
f3(rv3)
f5(rv3)
print("----------- End of the Program -------------")
