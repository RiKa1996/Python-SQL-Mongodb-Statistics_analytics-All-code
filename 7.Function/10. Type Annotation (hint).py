#
def add(a,b):
    print(a+b)

add(55,66)
add(12.33,33.22)
add("hi","hello")
#add(10,"hi")

print("------------------------------")
#Type Annotation (hint) (added in 3.5/3.6)--------ye hume hint deta hai. ydi hint ke bhi lagti hoti hai. to isme programmer ki ko galti
                                                  #nhi hai
def add(a:int,b:float):
    print(a+b)

add(55,66)
add(12.33,33.22)
add("hi","hello")
add(10,42.33)
add(23.5,55)
#add("hi",66)    #error type annotation 
print("------------------------------")

x=10
print(x)

x:int=200
print(x)

x:int="hi"
print(x)

x:list=[]
print(x)

x:float=56.3
print(x)
