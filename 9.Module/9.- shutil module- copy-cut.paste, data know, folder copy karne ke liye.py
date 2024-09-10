import shutil
#shutil.copy("modules.py","D:/modules.py")               #copy function sirf file copy kar ke paste karne ke liye hai.
#shutil.move("modules - Copy.py","d:/modules - Copy.py") #cut kar ke paste karne ke liye hai move function
#shutil.copytree("e:/myimgs","d:/abc")       #ye direct file ko copy kar ke past karta hai.
tup=shutil.disk_usage("C:\\")                #disk_usage fucntion checke karta hai kitne GB/MB/Usage ko check karta hai.
print(tup)
print(tup[0]/(1024*1024*1024))      #GB kitni bachi hui hai check krne ke liye
print(tup[1]/(1024*1024*1024))
print(tup[2]/(1024*1024*1024))
