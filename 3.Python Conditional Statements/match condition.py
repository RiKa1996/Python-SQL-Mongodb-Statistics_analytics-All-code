#match condition(added in 3.10 version)
option=2
match(option):
    case 1|2:                #case 1 wo ya case 2 ho.
        print("Rishav")      #isme multiple case kabhi nhi chalta
    case 2:
        print("Karan")
    case 3:
        print("Anil")
    case 1.1:
        print("Rajesh")
    case "hi":
        print("Manish")
    case _:
        print("invalid option")
print("user num.:",option)
#----------------------------------------------------------------

print()
a=int(input("enter 1st num:"))
b=int(input("enter 2nd num:"))
option=input("""Select an option:
1.Add
2.Mul
""")
match(option):
    case "1":
        print(a+b)
    case "2":
        print(a*b)
    case _:
        print("invalid option")
#-----------------------------------------------------------------
print()
a=int(input("enter 1st num:"))
b=int(input("enter 2nd num:"))
option=input("""Select an option:
1.Add
2.Mul
""")
if(option=="1"):
    print(a+b)
elif(option=="2"):
    print(a*b)
else:
    print("invalid option")
