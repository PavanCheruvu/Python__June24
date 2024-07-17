import time

def product_registration():
    global pname
    pname = input('Enter a product name:')
    pcode = input(f'Enter {pname} code number:')
    pcost = input('Enter a product Cost:')
    Qty = input('Enter No.of qty:')
    billing(pcode,pcost,Qty) # nested call with args

def billing(pcode,pcost,Qty=0):
    total = int(pcost) * int(Qty)
    tax = total * 0.12
    gs = total + tax
    Write_Operation(pcode,pcost,Qty,total,tax,gs)

def Write_Operation(pcode,pcost,Qty=0,total=0.0,tax=0,gs=0):
    Wobj = open('E:\\products.log','a')
    s=f'{pname}\t{pcode}\t{Qty}\t{total}\t{tax}\t{gs}'
    t=f'Billing time:{time.ctime()}'
    Wobj.write(s+' '+t+'\n')
    Wobj.close()

def main():
    for v in range(3):
        product_registration()
        time.sleep(2)
        print('') # empty line
            

main() # simple function call
