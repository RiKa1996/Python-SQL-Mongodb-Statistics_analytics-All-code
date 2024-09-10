#Parameters/ Arguments

def mul (a,b,r,s):     #Parameters   #jitne parameters honge utne hi arguments hone chaiye
    print(a*b*r*s)                   #jitne parameters honge utne hi arguments hone chaiye

mul(4,4,56,5)           #Arguments   #jitne parameters honge utne hi arguments hone chaiye
#print(a)                #NameError: name 'a' is not defined
mul(5,5,5,5,)
print('----------------------------------------------------------------------------------------')
#user se input lene per:
def mul(a,b):
    print(a*b)


x=int(input("enter 1st num:"))
y=int(input("enter 2nd num:"))
mul(x,y)
print('----------------------------------------------------------------------------------------')
#double parameters repeate nhi ho skte:    #but agruments repeate ho skte hai.
def mul(a,b):       #like this(a,a)
    print(a*b)

mul(4,4)
x=int(input("enter 1st num:"))
y=int(input("enter 2nd num:"))
mul(x,y)
print('----------------------------------------------------------------------------------------')
