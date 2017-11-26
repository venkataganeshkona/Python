"""
    write a function that takes an ordered list of numbers
    and another number. The function returns true if the given
    number is in the list
"""

aList = [1,3,5,8,9,10,12,25,256,310,310,800,3000]
elem = int(input("enter an element to search in the given list____>"))



def inList(alist,elem):
    if elem in alist:
        return True
    else:
        return False

print(inList(aList,elem))
    
