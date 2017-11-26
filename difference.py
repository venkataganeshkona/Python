"""
    write a program which takes a list and returns
    a new list containing all of the elements from the
    first list minus the duplicates
"""
list1=[1,3,4,5,6,7,21,17,25]
list2=[1,3,25,21,18,15,1,6,2,15]
newList=[]

def newList(list1,list2):
    newList=set(list1).difference(set(list2))
    return newList
print(newList(list1,list2))
