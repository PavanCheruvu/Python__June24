N = input('Enter a N value:')
 
if(N.isdigit()):
	N = int(N)
	r = N * 0.12
	total = r + N
	print(f"Total value is :{total} including 12% of {N}")
else:
	print(f"Sorry Given {N} is not a digits")
