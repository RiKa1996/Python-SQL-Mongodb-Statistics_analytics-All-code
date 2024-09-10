#Types of agruments
    #1. Positional Arguments
    #2. Keyword Arguments
    #3. Default Arguments

#use case of positional and keyword agruments
#============================================

def show(a,b):
    print(a,b)

show(3,b=4)         #function ko jab call krte hai. to phle position arg dete hai then keyword            
#show(a=3,20)       #errors      
#show(a=4,b=5,a=5)  #keyword agrument repeate nhi hota        
show(b=4,a=4)        
#show(10,a=20)      #TypeError: show() got multiple values for argument 'a'     

print("---------------------------------------------------------------------------------------")
#use case of default agruments
#==============================

def show (a,b=0,c=6):   #agar hum do se jyada defautl agrument dena chahte hai. to hume default agr. hi dena padega.
    print(a,c,b)

show(a=10,b=55)

print("---------------------------------------------------------------------------------------")
def show (a,b=0,c=6):   #agar hum do se jyada defautl agrument dena chahte hai. to hume default agr. hi dena padega.
    print(a,b,c)

show(a=10,b=55)
