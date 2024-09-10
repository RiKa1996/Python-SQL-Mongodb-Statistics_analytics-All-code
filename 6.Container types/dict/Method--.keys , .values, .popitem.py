d={(1,2):(1,2,3,4,5)}
print(d[(1,2)])
print(d)

#.keys method
d={101:'mango',102:'orange',103:'apple'}   #ye hume ek list jaisi tuple me wapas karta hai.
print(d.keys())              #dict_keys([101, 102, 103])

for k in d.keys():
    print(k)

#.values method
print(d.values())            #dict_values(['mango', 'orange', 'apple'])
print('orange' in d.values())#True
print('banana' in d.values())#False

for v in d.values():
    print(v)
print("-----------------------------------------------------------------")
#.popitem method
#---------------
#tup=d.popitem()    #ye hume delete huye item ek tuple me wapas deta hai.
#print(d,tup)       #aur ye dict ke last item ko hi delete karta hai.

k,v=d.popitem()
print(d,k,v)
