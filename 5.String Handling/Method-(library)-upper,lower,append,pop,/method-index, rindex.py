#index Method
s="abcdefghijebklmnopqbrsetuvwxybzb"
print(s.index("b",0)) #by default 0 index se find karta hai
print(s.index("b",0)) #positive-first wala-agar ko charactor nhi mila to error
#print(s.index("B")) #error
print(s.index("b",2)) #ab 2 index se find karega

print("-----------------------------------------------")
#rindex Method-(right index)
print(s.rindex("e"))  #right index
print(s.rindex("b"))  #right index
print(s.rindex("p"))













print("-----------------------------------------------")
#operator
s="abazabca"
print(s)
#index operator
#prefix[index]

ch=s[3]
print(ch,type(ch))

ch=s[-1]
print(ch,type(ch))

ch=s[0]
print(ch,type(ch))
#print(s[54])       #error

