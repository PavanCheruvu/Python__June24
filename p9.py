app = input('Enter an app name:')
port = input(f'Enter {app} port number:')
		
if(int(port) >5000 and int(port) <6000):
    print(f'App {app} port  {port}')
else:
    app = 'TestApp'
    port = 8080
    print(f'App {app} port {port}')
