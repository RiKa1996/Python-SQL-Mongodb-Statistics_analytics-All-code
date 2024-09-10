#pattern logic
#tyr to use nested loops
#outer loop controls num of rows and nested loop
#controls num of cols in each row
#always print the pattern horizontally

print("-----------------------------")
num=int(input("enter num"))
for x in range(1,num+1):
    for y in range(1,x):
        print("*",end=" ")
    print()
print("-----------------------------")
num=int(input("enter num"))
for x in range(1,num+1):
    for y in range(1,x*2):
        print("*",end=" ")
    print()
print("-----------------------------")
num=int(input("enter num"))
for x in range(num-1,0,-1):
    for y in range(x):
        print("*",end=" ")
    print()
print("-----------------------------")
num=int(input("enter num"))
for x in range(0,num):
    for y in range(0,num-x-1):
        print(end=" ")
    for y in range(0,2*x+1):
        print("*",end="")
    print()
print("-----------------------------")
num=int(input("enter num"))
for x in range(num,0,-1):
    for y in range(0,num-x):
        print(end=" ")
    for y in range(0,x):
        print("*",end=" ")
    print()
