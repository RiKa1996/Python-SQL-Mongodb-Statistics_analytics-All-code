#strip Method   #space ko hatane ke liye
s=" virat kohali "
print(s.strip())

#rstrip Mehtod (right strip method)
s=" rishav kumar "
print(s.rstrip())

#lstrip Mehtod (left strip method)
s=" rishav kumar "
print(s.lstrip()) #("--------------------------------------------------")
u=input("enter username:")
p=input("enter password:")
u=u.lower()
u=u.rstrip()
u=u.lstrip()
if(u=="india" and p=="admin"):
    print("valid")
else:
    print("invalid")
