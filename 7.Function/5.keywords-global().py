a=5   #global variable
b=4   #global variable

def mul():
    global a,b   #global keyword ka use karne se jo local variable hai wo bhi global ban jate hai.
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

#Scope:
#1. Local scope------local scope banane ke liye def ke ander likhna padta hai.
#2. Global scope-----global scope banane ke liye hume def ke bahar aur top level pe likhna padta hai.
