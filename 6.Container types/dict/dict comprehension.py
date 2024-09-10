#dict comprehension
#var={key_expresion:value:expresion for}

d={i:i*i for i in range(5)}
print(d)


#user se input le ke
d={float(input("enterv key")):input("enter value") for i in range(1,5)}
print(d)
