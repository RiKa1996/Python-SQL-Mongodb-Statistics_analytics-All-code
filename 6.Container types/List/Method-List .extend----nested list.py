#extend-method
x=[10,20,30,40]
y=[60,50,80,90]

x.extend(y)
print(x)     #extend sabhi ko merge kar deta hai.
print("---------------------------------------------------------")

x=[10,20,30,[40,50,60,]]   #nested list
print(len(x))
print(x[0])
print(x[-1])
print(x[-1][0])
