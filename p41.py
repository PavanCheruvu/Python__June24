class product:
    pid = 101
    pname = 'prodA'

class customer(product): # single inheritance
    price = '1000Rs'
    #pid = 505 # duplicate parent attribute - overwrite
    pid = product.pid 
    
obj = customer()
print(obj.pid,obj.pname,obj.price)
