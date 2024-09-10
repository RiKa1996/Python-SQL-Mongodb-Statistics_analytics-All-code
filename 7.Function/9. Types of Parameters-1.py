#Positional only parameters
#==========================
def show(a,b,/):       #agar hum function ke parameters ke last me slase laga dete hai. to wo positional only pars. ban jate hai.
    print(a,b)         #phir hum isme kuch aur jaise keyword agrument ka use nhi kar skte

show(55,66)
#show(a=99,b=88)       #error

#Keyword only parameters
#=======================

def show(*,a,b):
    print(a,b)

#show(77,55)           #error
show(a=33,b=95)        #ydi hum function ke aage stract laga dete hai. to wo sirf keyword only pars. per hi kam karta hai.


#Positional or Keyword only parameters
#=====================================

def show(a,b):
    print(a,b)

show(69,96)
show(a=89,b=52)
show(55,b=64)
#show(a=63,77)    #error kyoki sbse phle positional and the keyword

print("------------------------------------------------------------")
def show(a,b,/,c,d,*,e,f):
    print(a,b,c,d,e,f)

show(23,52,66,d=88,e=44,f=58)
#show(23,52,c=66,88,e=44,f=58)   #error kyoki sbse phle positional and then keyword
