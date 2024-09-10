#String formatting-->using var/expression in string
a=int(input("enter 1st num:"))
b=int(input("enter 2nd num:"))
msg="multiply of a and b=a*b"
print(msg)

#1st way (using format specifiers)
msg="multiply of %f and %f=%.2f"%(a,b,a*b)  #f means float num
print(msg)

msg="multiply of %d and %d=%.2f"%(a,b,a*b)  #d means integer num
print(msg)

#2nd way (using positional parameters)
msg="multiply of {0} and {1}={2}".format(a,b,a*b)
print(msg)

msg="multiply of {1} and {2}={1}".format(a,b,a*b)
print(msg)

msg="multiply of {1} and {1}={0}".format(a,b,a*b)
print(msg)

#msg="multiply of {1} and {2}={3}".format(a,b,a*b)   #error
#print(msg)

#3rd way (using named parameters)
msg="multiply of {a} {b}={c}".format(a=a,b=b,c=a*b)   #isme name dena hota hai.
print(msg)

msg="multiply of {x} {y}={z}".format(x=a,y=b,z=a*b)   #isme name dena hota hai.
print(msg)
 
#4th way (using f-string) added in 3.6                # f- string aage likhna padta hai.
msg=f"multiply of {a} and{b}={a*b}"
print(msg)

















