d1={'a':'apple','b':'bat'}
d2={'a':'android',"c":"cat"}
d3={}
k1=list(d1.keys())
k2=list(d2.keys())
k3=sorted(set(k1+k2))
print(k3)


for k in k3:
    if(k in d1.keys() and k in d2.keys()):
        d3[k]=[d1[k],d2[k]]
    elif(k in d1.keys()):
        d3[k]=d1[k]
    else:
        d3[k]=d2[k]
print(d3)
