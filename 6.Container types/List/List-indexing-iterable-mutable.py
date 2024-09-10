x=[]
print(type(x))

x=[10,20,30,10,20,15.3,"hello"]
print(type(x),x)

#indexing
print(x[0])
print(x[-1])

#iterable
for i in x:
    print(i)

print("-------------------------------------------------------------")
s1=5222
s2=6528
s3=8755

x=[s1,s2,s3,6584]
print(min(x))
print(max(x))
print(sum(x))
print(len(x))
print(sum(x)/len(x))
print(sorted(x))               #assending order
print(sorted(x,reverse=True))  #desending order
print(x)
print("-------------------------------------------------------------")
#mutable/modifiable
x=[10,20,30,]
print(x)
x[0]=100
print(x)
























