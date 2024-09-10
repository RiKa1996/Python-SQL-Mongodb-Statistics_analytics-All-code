#Note-->only immutable values/types are allowed in set

s={10,20.5,"hi",(1,2)}      #set me tuple allowed hai.
print(s)

#s={10,20.5,"hi",(1,2),[1,2]}      #set me list  allowed nhi hai.
#print(s)

s=[10,20.5,"hi",(1,2),[],{1,2}]      #list me tuple,list,set  allowed hai.
print(s)

s=(10,20.5,"hi",(1,2),[],{1,2})      #tuple me tuple,list,set  allowed hai.
print(s)
