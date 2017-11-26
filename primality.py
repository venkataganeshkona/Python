"""
    ask the user for a number.
    return true or false depending
    if it is prime
"""


a = int(input("enter a number to test its primality: "))

def is_prime(a):
    return a > 1 and all(a % i for i in range(2, int(a**0.5) + 1))
print(is_prime(a))
