#fruits()         #NameError: name 'fruits' is not defined
def colors():               
    print("green")          
    print("blue")
    fruits()     #ek function se dusre fucntion me call kiya ja skta hai.
    
def fruits():
    print("apple")
    print("mango")
    #colors()    #ye infinite ho jayega
colors()
fruits()

print("--------------------------------------------------------------------")
def name():
    print("karan")
    print("rishav")
    #name()     #ye infinite mode me chala jayega   #because of "recursion"
name()

print("--------------------------------------------------------------------")
def animals():
    print("dog")
    print("cat")
#animals()           

def animals():      #ydi humhari def ka same name ke hai to jo latest def hogi wo exicute ho jayega.
    print("Lion")
    print("tiger")

animals()
print("--------------------------------------------------------------------")






