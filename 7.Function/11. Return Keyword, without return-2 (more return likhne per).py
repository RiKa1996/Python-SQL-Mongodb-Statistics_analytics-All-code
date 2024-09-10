#more return karne per hume sirf kewal sbse phle wali ki return value milti hai.
def airthmetic(a,b):
    c=a*b
    d=a-b
    e=a/b
    return c
    return d
    return e

res=airthmetic(6,5)
print(res)
print("---------------------------------------------------------------------------")
#ydi hume more return value chaiye to hume phle wali return me list , tuple ,dict,set me kisi ek me rakh ke value ko le skte hai.
def airthmetic(a,b):
    c=a*b
    d=a-b
    e=a/b
    #return [c,d,e]
    return {"mul":c,"minus":d,"div":e}
res=airthmetic(6,5)
print(res)
print("---------------------------------------------------------------------------")
#loop lagane per:     #loop lagane per bhi sirf phla return chal ke band ho jata hai.
#===============
def mul(a,b):
    c=a*b
    for i in range(5):
        return c*i     #0
res=mul(6,5)
print(res)
