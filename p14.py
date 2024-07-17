filenames = [] 
print(f"A: Total no.of files:{len(filenames)}")

c=0
while(c < 5):
	fname = input("Enter a filename:")
	filenames.append(fname) # adding input to an existing list
	c=c+1


print("List of files:-")
for v in filenames:
	print(v)

print(f"B: Total no.of files:{len(filenames)}")
