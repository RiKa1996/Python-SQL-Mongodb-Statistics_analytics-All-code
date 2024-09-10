#os module  operating system
import os
print(os.getcwd())      #E:\New folder (2)\9.Module #ye current working directry me jaha run ho rha hai uska address lata hai.
names=os.listdir()
print(names)            #listcwd folder sari file ko print karta hai.
print(len(names))       #jitni bhi file folder me hai. uski count kar deta hai.

for n in names:
    print(n)
print("----------------------------------------------")
#kisi dusre file ke elements bhi search kar skta hai.
#----------------------------------------------------
names=os.listdir("D:\DUCAT CLASSES-2")     #ye dusre kisi file ka bhi search kar skta hai.
print(names)            #listcwd folder sari file ko print karta hai.
print(len(names))       #jitni bhi file folder me hai. uski count kar deta hai.

for n in names:
    print(n)

print("----------------------------------------------")
#file ko search karne ke liye. cwd me wo file hai ya nhi True/False
#-------------------------------------------------------------------
print(os.path.exists("D:\DUCAT CLASSES-2"))            #True    kyoki ye file hai
print(os.path.exists("E:/New folder (2)"))             #True
print(os.path.exists("E:/Machin Learning/5-oct"))      #False   ye file nhi hai.

print("----------------------------------------------")
#file ko rename karne ke liye
#----------------------------
os.rename("E:/New folder (2).text","E:/New folder (2).rishav")                        #os.rename(jo hai file, jo name rakhna hai.)
