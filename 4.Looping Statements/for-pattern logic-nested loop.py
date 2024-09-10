#pattern logic
#tyr to use nested loops
#outer loop controls num of rows and nested loop
#controls num of cols in each row
#always print the pattern horizontally

for x in range(2,5):#2,3,4
    for y in range(1,4):#1,2,3
        print(x*y,end=" ")
    print()
print("-----------------------------")
for x in range(6,1,-1): #6,5,4,3,2,
    for y in range(1,x):  #1
        print(y,end=" ")
    print()

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
