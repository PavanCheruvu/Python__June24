class product:
    pid = 101
    pname = 'prodA'

class customer(product): # single inheritance
    price = '1000Rs'

obj = customer()
print(obj.pid,obj.pname,obj.price)
