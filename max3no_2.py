#Find max b/w 3 number
#max3no_2.py
#if..else condition 
#accepting
a = int(input("Enter 1st number"))
b = int(input("Enter 2nd number"))
c = int(input("Enter 3rd number"))

if (a > b and a>c):
	print("{} is big".format,a)
elif (b > c):
	print("{} is big".format,b)
else:
	print("{} is big".format,c)

print("Program Finished")