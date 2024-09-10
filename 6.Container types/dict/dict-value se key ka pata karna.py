d={1:'a',2:'b',3:'a',4:'c',4:'a'}
print(d)

x=[]
for k,v in d.items():
    if(v=='a'):
        x.append(k)
print(x)
print("---------------------------------------------")
x=[]
for k,v in d.items():
    if(v=='b'):
        x.append(k)
print(x)

print("---------------------------------------------")

x=[]
for k,v in d.items():
    if(v=='z'):
        x.append(k)
print(x)
