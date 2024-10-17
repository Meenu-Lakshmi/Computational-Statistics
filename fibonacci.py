import math
def is_perfectsquare(n):
	s=int(math.sqrt(n))
	return s*s==n
def is_fibonacci(x):
	return is_perfectsquare(5*x*x-4) or is_perfectsquare(5*x*x+4)
a=int(input("Enter the number: "))
if is_fibonacci(a):
	print("Fibonacci number")
else:
	print("not fibonacci")
