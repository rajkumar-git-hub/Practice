
'''
import module
import module as m1
import module1,module2

from module import member1, member2
from module import member1 as m1, member2 to m2
'''


import central

print(dir(central))     #dir() - It is a function - It return all module mem in the form of list.
print(central.tax)
print(central.get_discount())   #print(module.member)
