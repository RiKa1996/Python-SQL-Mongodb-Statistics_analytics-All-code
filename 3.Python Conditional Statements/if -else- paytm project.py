amt=int(input("enter amt"))
if(amt>=1000):
    amt=amt-50
    print("50 cashback added:")
    pc=input("enter promocode:")
    if(pc=="india"):
        amt=amt-50
        print("50 more cashback added")
    else:
        print("invalid promocode")
print("Final Amount:",amt)
