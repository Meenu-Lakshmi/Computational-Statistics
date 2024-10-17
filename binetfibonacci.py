import numpy as np

def fibonacci_binet(n):
    
    phi = (1 + np.sqrt(5)) / 2
    psi = (1 - np.sqrt(5)) / 2
    
    fib_numbers = (np.round((np.power(phi, np.arange(n)) - np.power(psi, np.arange(n))) / np.sqrt(5))).astype(int)
    
    return fib_numbers


n = int(input("Enter number of fibonacci numbers to display: "))
fib_series = fibonacci_binet(n)

print(fib_series)
