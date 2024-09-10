s="abccdbbaacedffaa"
#slicing--->extracting substring based on pos
#prefix[start_pos:end_pos:step]
#start_pos--->inclusive,end_pos--->exclusive
print(s[1:20:2])
print(s[0:9:1])
print(s[-8:9:2]) #a
print(s[-1:3:1]) #empty#
print(s[7:0:-1]) #abbdccb
print(s[-1:3:-1])#aaffdecaabbd
print(s[1:5:1])  #bccd
print(s[::-1])   #aaffdecaabbdccba
print(s[::1])    #abccdbbaacedffaa
print(s[::])     #abccdbbaacedffaa
print(s[0:6:-1]) #empty#
print(s[0:6:])   #abccdb                           #by default step is positive direction
print(s[:9:])    #abccdbbaa                        #start 0 and step positive direction
print(s[::-1])   #aaffdecaabbdccba                 #start -1 and end 0 negative direction
print(s[1::])    #bccdbbaacedffaa                  #end -1 and step is not given so by default positive derection
print(s[::])     #abccdbbaacedffaa                 #start 0 and -1 and by default positive direction

print("------------------------------------------------------------")
#some question
s="abababca"
x=0
for i in s:
    x+=1
    if(i=="c"):
        print(i,x)
print("------------------------------------------------------------")
s=" a b  c d e "
ss=""
for i in s:
    if(i==" "):
        pass
    else:
        ss=ss+i
print(ss)
print("------------------------------------------------------------")
s="abccdbbaacedffaa"
print(s[0].upper()+s[1:-1]+s[-1].upper())  ##1
print(len(s))                              ##2

count=0                                    ##3
for i in s:
    count+=1
print(count)


























