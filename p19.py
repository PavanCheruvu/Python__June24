import time
pin = 1234

count = 0
while(count <3):
    p = input('Enter a pin Number:')
    count = count + 1
    if(int(p) == pin):
        print(f'Success pin is matched - {count} - Entry Time:{time.ctime()}')
        break
    else:
        print(f'Sorry pin {p} is not-matched - Entry Time:{time.ctime()}')

if(pin != int(p)):
    print("Sorry your pin is blocked")
    print(f'pin blocked time is :{time.ctime()}')
