def dec_to_bin(dec):
	decimal=int(dec)
	print("binary number :",bin(decimal))
def dec_to_hexa(dec):
	decimal=int(dec)
	print("hexadecimal number :",hex(decimal))
def dec_to_oct(dec):
	decimal=int(dec)
	print("octal number :",oct(decimal))
dec=int(input("Enter the number: "))
dec_to_bin(dec)
dec_to_hexa(dec)
dec_to_oct(dec)
