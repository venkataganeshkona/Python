"""
   take two example lists and write a program
   that returns a list that contains only the
   elements that are common between the lists.
   Make sure your progam works on different
   size lists. Write this using one list comp-
   rehension.
"""

import random
a = random.sample(range(1,50),10)
b = random.sample(range(1,50),10)
print ([x for x in set([a if len(a)>len(b)
        else b][0])
        if (x in set(a)) and (x in set(b))])
