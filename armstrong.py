x=int(input("Enter the number: "))
n=len(str(x))
temp=x
sum=0
while(x>0):
	a=x%10
	sum=sum+(a**n)
	x=x//10
if sum==temp:
	print(temp," is armstrong number")
else:
	print("Not armstrong")
