"""
    given a list saved in a variable return
    a new list of all the even elements
"""

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
c=[x for x in a if x%2==0]
print(c)
