def mul(a,b):    #print(c) ko print krne ke liye global ek shi tarika nhi hai
    global c
    c=a*b
    print(c)

mul(2,5)
print(c)

#return keyword
#==============
def mul(a,b):    
    
    c=a*b
    print(c)
    return c    #return c likhne per print(res) ho jata hai.
res=mul(2,5)
print(c)
print("-----------------------------------------------------------------------")
def mul(a,b):    
    
    c=a*b
                #ydi humne return keyword nhi likhne per hume none value return hoti hai.
res=mul(2,5)
print(res)

print("-----------------------------------------------------------------------")
def mul(a,b):    
    
    c=a*b
    return      #ydi humne return keyword likha hai. but uske aage humne batya nhi kya return karna to hume None value milti hai.
res=mul(2,5)
print(res)
