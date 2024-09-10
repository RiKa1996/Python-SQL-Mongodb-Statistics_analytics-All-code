a=[]
b=()
c={}
d={10}
print(type(a))
print(type(b))
print(type(c))
print(type(d))

s=set()
print(type(s),len(s))

s=set("india")
print(s)

s=set(range(1,52))
print(s)

x=[10,20,30,]    #list , set me convert ho skta hai.
s=set(x)
print(s)

x=(10,20,30)    #tuple , set me convert ho skta hai.
s=set(x)
print(s)

x={10,20,30}    #set , tuple me convert ho skta hai.
s=tuple(x)
print(s)

x={10,20,30}    #set , list me convert ho skta hai.
s=list(x)
print(s)
