import time

wobj = open('E:\\pin_history.log','a')

pin = 1234

count = 0
while(count <3):
    p = input('Enter a pin Number:')
    count = count + 1
    if(int(p) == pin):
        wobj.write(f'Success pin is matched - {count} - Entry Time:{time.ctime()}\n')
        print(f'Success pin is matched - {count} - Entry Time:{time.ctime()}')
        break
    else:
        wobj.write(f'Sorry pin {p} is not-matched - Entry Time:{time.ctime()}\n')

if(pin != int(p)):
    print("Sorry your pin is blocked")
    wobj.write(f'pin blocked time is :{time.ctime()}\n')

wobj.close()
