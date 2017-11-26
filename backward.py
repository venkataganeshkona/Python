"""
    create a function that takes in a string and
    returns the string in reverse order. For example
    'my name is andy' returns 'andy is name my'
"""

string = input("please enter a sentence to reverse____>> ")
               
def backward(string):
    a = string.split(' ')
    a.reverse()
    return a

print(backward(string))

    
