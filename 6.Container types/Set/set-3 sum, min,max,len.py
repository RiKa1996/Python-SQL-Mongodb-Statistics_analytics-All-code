s={10,5,20,3,3}
print(sum(s))
print(max(s))
print(min(s))
print(len(s))
print(sorted(s)) #[3, 5, 10, 20] #sorted function hamesha ek list me hi deta hai.
print("------------------------------------------------------------------------")

s1={10,20,30}
s2={30,40,50}
#s3=s1+s2
#print(s3)    #TypeError: unsupported operand type(s) for +: 'set' and 'set'
s3=s1.union(s2)
print(s3)
