#file ko rename karne ke liye
#----------------------------
import os
#os.rename("E:/New folder (2)/text.txt","E:/New folder (2)/student.txt")       #os.rename(jo hai file, jo name rakhna hai.)
names=os.listdir("E:/New folder (2)/text")
#print(names)

#bahot sari file ka name change karne ke liye banaya gaya hai
#-------------------------------------------------------------
i=1
for n in names:
    #print(n)
    os.rename(f"E:/New folder (2)/text/{n}",f"E:/New folder (2)/text/{i}.txt")
    i+=1
print("taxk compleated")

print("------------------------------------------------------")
