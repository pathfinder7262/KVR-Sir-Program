#Find max b/w 3 number
#max3no.py
#Simple if condition 
#accepting
a = float(input("Enter 1st number"))
b = float(input("Enter 2nd number"))
c = float(input("Enter 3rd number"))
big = a
if (b > big):
	big=b
if (c > big):
	big=c
print("{} is biggest number".format(big))

	