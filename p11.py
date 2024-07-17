
user_name = input('Enter a username:')

if(len(user_name) == 0):
	print('Sorry your input is missing')
else:
	print(f'Hello {user_name}')
		
print('') # empty line

user_name = input('Enter a username:')

if(user_name): # bool(Value) ->True/False
	print(f'Hello {user_name}')
else:
	print('Sorry your input is missing')
