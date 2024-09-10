#sys module value ka size batata hai.bits me (dynamic size hota hai.)

import sys
print(sys.getsizeof(10))               #getsizeof fucntion value ka size hume bits me deta hai. aur ye dynamic size hote hai.jo
print(sys.getsizeof(6495963232695945632656))     #hume phle se pata nhi hota hai.
print(sys.getsizeof([]))
print(sys.getsizeof(()))

print(sys.maxsize)            #maxsize variable hume , koi bhi value ka maximum size jitna ho skta hai. wo hume dega. 

#print(sys.exit())     #exit function karne per aage ka code print hona band ho jata hai.
#print("bye")
print(sys.hexversion)
