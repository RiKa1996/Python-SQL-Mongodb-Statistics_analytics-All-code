#tuple-->it is immutable/unmodifiable version of list  (,)ye coma jaruri hai.
x=()
print(type(x))

x=tuple()
print(x)

x=tuple("india")
print(x)

#range function pass karne ke liye
x=tuple(range(1,11))
print(x)

#tuple copy karne ke liye
x=[10,20,10,30,40,50]
y=tuple(x)
print(x)

x=(10,20,30,10,40,50,60,10,20,80)
print(min(x))
print(max(x))
print(sum(x))
print(30 in x)
print(sorted(x,reverse=True))
y=sorted(x)
print(y)
print(sorted(x,reverse=True))

#user se input lene pe
a=int(input("enter value-1:"))
b=int(input("enter value-2:"))

t=(a,b)
print(t)

#2 tuple ko plus karne per
a=(10,20,30,)
b=(50,60,30,4,)
t=a+b
print(t)
























