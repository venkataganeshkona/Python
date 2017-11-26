"""
  password generator in python. Must contain lowercase letters, 
  uppercase letters, numbers, and symbols. Include your run-time 
  code in a method.
"""
import random
def password():
    upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    a = random.choice(upperCase)
    b = random.choice(upperCase)
    
    lower = "abcdefghijklmnopqrstuvwxyz"
    c = random.choice(lower)
    d = random.choice(lower)

    numbers = "0123456789"
    e = random.choice(numbers)
    f = random.choice(numbers)
    
    symbols = "~!@#$%^&*()_+-={ }|[]\:<>?,."
    g = random.choice(symbols)
    h = random.choice(symbols)
    
    password = [a,b,c,d,e,f,g,h]
    random.shuffle(password)
    password = "".join(password)
    
    return password

createPass = input("press 1 to create password or any other key to exit___> ")
if(createPass == '1'):
   print(password())
else:
   print("you have ended program")
   
  
  
  
