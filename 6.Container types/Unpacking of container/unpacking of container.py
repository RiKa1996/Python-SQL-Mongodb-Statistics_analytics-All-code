#Unpacking of container
x=[10,20,30,44]
print(x)

*a,b,c,d=x     #jitni value container me hai utne hi humhare variable hone chaiye
print(a)
print(b)
print(c)

print("--------------------------------------------------------------------------------")
y=[22,5,2,78]
*a,b,c,d=y
print(a)
print(b)
print(c)
print(d)
print("--------------------------------------------------------------------------------")
y=[10,20,30,40]   
a,*b,c,d=y
print(a)
print(b)
print(c)
print(d)
print("--------------------------------------------------------------------------------")
y=[65,52,4,51]
a,*b=y
print(a)
print(b)
print("--------------------------------------------------------------------------------")
y=[1,2,3,4]
*a,b=y
print(a)
print(b)
print("--------------------------------------------------------------------------------")
y=[1,2,3,4]
#*a,*b=y         #do ko strite dene pe error dega
print(a)
print(b)
