x=[10,20,30,40,10,50,70,10]
print(x)

#del(x)
#.pop
v=x.pop(1)
print(x,v) #jo delete hua wo batata bhi hai.

v=x.pop()
print(x,v) #.pop method last elements ko delete karta hai autometic. 10

#.remove method
#---------------
x.remove(50)
print(x)

x.remove(10)
print(x)        #kewal first wala remove hoga

x.remove(10)
print(x)
#x.remove(100)
#print(x)       #error
print("------------------------------------------------------------------")
while(10 in x):
    x.remove(10)
print(x)
print("------------------------------------------------------------------")
print(100 in x) 
print(70 in x)
print("------------------------------------------------------------------")
#differences
#del
#----
#1.operator
#2. removes value on given index
#3. we have to specify index

#pop
#---

#1. method
#2. removes and return value on given index
#3. if we do not specify index, removes last value/elements


