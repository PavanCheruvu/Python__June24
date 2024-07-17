sh_var = input('Enter a shell name:')

if(sh_var == 'bash'):
    Fname = "/etc/bashrc"
elif(sh_var == 'ksh'):
    Fname = '/etc/kshrc'
elif(sh_var == 'psh'):
    Fname = 'C:\\winprofile'
else:
    sh_var = '/bin/nologin'
    Fname = '/etc/profile'

print(f'Shell name is:{sh_var} profile filename:{Fname}')
