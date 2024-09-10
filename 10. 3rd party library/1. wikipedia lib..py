import wikipedia as wk
#result=wk.summary("python language")
#print(result)

#result=wk.summary("raul costa")
#print(result)
text=input("enter text:")
result=wk.summary(text,sentences=3)
print(result)
