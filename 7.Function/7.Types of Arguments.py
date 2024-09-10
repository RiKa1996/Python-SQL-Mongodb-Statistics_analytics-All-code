#Types of agruments
    #1. Positional Arguments
    #2. Keyword Arguments
    #3. Default Arguments

def show(a,b):
    print(a,b)

show(3,4)            #Positional Arguments
show(a=3,b=4)        #Keyword Arguments   3 4
show(b=3,a=4)        #Keyword Arguments   4 3
show(b=4,a=3)        #Keyword Arguments   3 4

print("--------------------------------------------------")
def txn(frm,to,amt):
    print(frm,to,amt)

txn(to=101,frm=100,amt=5000)    #Keyword Arguments  #100 101 5000     
txn(frm=100,to=101,amt=5000)    #Keyword Arguments  #100 101 5000

print("--------------------------------------------------")

def fruits(A="Mango",B="Apple"):
    print(A,B)

fruits()             #Agar jb hum call karge aur agruments kuch nhi likha hai to by default jo parameter me agruments considered
fruits("Apple")             #huye hai whi aa jata hai.
