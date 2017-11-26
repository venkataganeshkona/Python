"""
    ask the user for a string. if it is
    a palindrome print true or false
"""

palindrome = input("Are you a palindrome......>>> ")

def checker(palindrome):
    if palindrome[::-1]==palindrome:
        print("Yes I am a palindrome")
    else:
        print("No I am not a palindrome")
    
checker(palindrome)
    
