import math
def prime(n):
	flag=True
	if n<=1:
		print("neither prime nor composite")
		return None
	for i in range(2,int(math.sqrt(n)+1)):
		if n%i==0:
			flag=False
			break
	if(flag):
		return True
	else:
		return False
	
x=int(input("Enter starting interval : "))
y=int(input("Enter stop interval : "))
for i in range(x,y+1):
	if prime(i):
		print(i)
