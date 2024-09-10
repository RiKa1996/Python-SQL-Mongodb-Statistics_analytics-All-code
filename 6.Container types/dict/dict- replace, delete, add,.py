#dict

d={101:"sonu",500:"monu",201:"sonu"}
print(d)        
print(d[500])    #indexing wala kam kar deta hai. but sirf key ke liye na ki value ke liye.
#print(d[2011])

print(500 in d )    #True  in operator sirf key ke liye kam karta hai. na ki value ke  liye.
print('sonu' in d)  #False  ye value ko support nhi karta hai.

#dict me replace karna
d[101]="virat kohli"
print(d)

#elements ko add karna
d[102]="rishav kumar"    #but ye dict ke last me ja ke add ho jayega.
print(d)

#delete karne ke liye
del d[500]   #del se key aur value dono delete ho jata hai.
print(d)

v=d.pop(101) #pop se jo delete hota wo hume batata bhi hai.
print(d,v)

#.popitem method
#---------------
#tup=d.popitem()    #ye hume delete huye item ek tuple me wapas deta hai.
#print(d,tup)       #aur ye dict ke last item ko hi delete karta hai.

k,v=d.popitem()
print(d,k,v)
