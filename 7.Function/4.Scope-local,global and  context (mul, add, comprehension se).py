a=5   #global variable
b=4   #global variable

def mul():
    a=9          #ydi global me bhi hai. aur local me bhi hai. to phle priority local ko di jati hai.
    b=6
    c=a*b
    print(c)

def add():
    d=a+b
    print(d)

mul()
add()     #dubara def ka answer ke liye global scope pe hona chaiye
#print(c) #error
print("----------------------------------------------------------------")
x=[i*i for i in range(5)]
print(x)
#print(i)  #ydi ye context scope hota to ye print ho jata.

for j in range(5):
    pass            #Local variable
print(j)

if (True):
    k=10            #Global variable
print(k)

z=10                #Global variable
print(z)

#Scope:
#1. Local scope (var of function)------local scope banane ke liye def ke ander likhna padta hai.
#2. Global scope (if a var is not local & context)-----global scope banane ke liye hume def ke bahar aur top level pe likhna padta hai.
#3. Context scope (var of comprehension)--- ye sirf comprehension me use kiya ja skta hai.
