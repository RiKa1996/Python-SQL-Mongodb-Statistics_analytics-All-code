#tuple-->it is immutable/unmodifiable version of list  (,)ye coma jaruri hai.
x=()
print(x)
print(type(x))
x=(10,20,30)
print(type(x),x)        #<class 'tuple'> (10, 20, 30)

x=(10)
print(type(x),x)        #<class 'int'> 10

x=(10,)
print(type(x),x)        #<class 'tuple'> (10,)

x=10,23,30
print(type(x),x)


print(x[0])             #indexing hoti hai.
#x[0]=100         #TypeError: 'tuple' object does not support item assignment
#del x            #delete ho jata hai.
print(x)                #NameError: name 'x' is not defined


#del x[0]         #TypeError: 'tuple' object doesn't support item deletion
