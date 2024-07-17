

c=0
while(c < 5):
    login = input('Enter a login name:')
    if(login == 'root'):
        print('Login is matched')
        break # exit from loop
    else:
        print('Login is Not matched')
    c=c+1
