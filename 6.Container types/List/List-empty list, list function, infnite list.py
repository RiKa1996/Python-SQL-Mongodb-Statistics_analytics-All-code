#list()-list function
x=list()
print(x)

x=[]
print(x)

x=list("india")
print(x)          #['i', 'n', 'd', 'i', 'a']

#range function se
x=list(range(1,11))
print(x)

x.append("bharat")
print(x)         #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'bharat']

#list ko copy karne ke liye
y=list(x)
print(y)

print("-------------------------------------------------")
x=[10,20,30,40,]
for i in x:
    x.append(i)
    print(x)          #enfinite time chalega
