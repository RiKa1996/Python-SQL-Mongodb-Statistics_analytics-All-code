import itertools
x=[0,1,2]
c=itertools.combinations(x,r=3)          #combinations function me kewal ek combination deta hai.
for i in c:
    print(i)
print("---------------------------------------------------------------------------")
c=itertools.permutations(x,r=3)          #permutaions function me sare possible case de deta hai.
for i in c:
    print(i)

print("---------------------------------------------------------------------------")
x=[0,1,2,3,4,5,6,8,7,9]
c=itertools.product(x,repeat=3)          #product function me sare possible case de deta hai. product function se value
for i in c:                              #repeat ho jati hai.
    print(i)

    
