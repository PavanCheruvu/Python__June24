
p1 = input('Enter a disk partition:')
s1 = input(f'Enter {p1} Size:')
p2 = input('Enter another partition:')
s2 = input(f'Enter {p2} Size:')

total = int(s1) + int(s2)

print(f'''
-------------------------------------
Partition:{p1}	Size:{s1} GB
Partition:{p2}	Size:{s2} GB
-------------------------------------
	Total	Size:{total} GB
-------------------------------------''')
