#refrence copy vs shallow copy vs deep copy

x=[10,20,30,40,50,[60,40,70,80]]
a=x                              #refrence copy
b=x.copy()                       #shallow copy



import copy
c=copy.deepcopy(x)               #deep copy

print(x)
print(a)
print(b)
print(c)

x[0]=500
print(x)
print(a)       #refrence copy hi change hua #kyoki x refrene hai.a=(refrence copy ka)
print(b)       #shallow copy nhi
print(c)       #deep copy bhi nhi

x[5][0]=12000
print(x)
print(a)       #refrence copy hi change hua #kyoki x refrene hai.a=(refrence copy ka)
print(b)       #is bar shallow copy bhi change hua   #kyoki yha b is also shallow copy of x
print(c)       #deep copy in dono ke case me change nhi hota.
