#set
x=set()
print(x)

s={10,5.5,"hi",10,True,10}
print(s)

#indexing
#print(s[0])                     #TypeError: 'set' object is not subscriptable

for i in s:
    print(i)

#s.insert(50)                     #AttributeError: 'set' object has no attribute 'insert'

#.add method
#-----------
s.add(500)
print(s)         #{True, 5.5, 10, 500, 'hi'}

s.pop()
print(s)         #{5.5, 'hi', 10, 500}

if(10 in s):
    s.remove(10)
print(s)

