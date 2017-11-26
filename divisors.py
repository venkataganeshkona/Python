"""
    ask the user for a number.
    return a list of all possible divisors.
"""

x = int(input("enter a number to print divisors for: "))

i = 1
while i<x:
   if x%i == 0:
      print (' divisor '  ,i)
   i = i + 1
print(' divisor ' ,x)
