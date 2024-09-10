#folder ko delete karne ke liye
import os

#os.rmdir("abc2")   #abc2 folder delete ho gai hai. isliye wha nhi hai

#Note: rmdir sirg khali forder ko delete karta. kisi folder ke ander folder ya koi bhi file wo us folder delete nhi karega
#------
#os.rmdir("pqr") #The directory is not empty: 'pqr'

import shutil
shutil.rmtree("pqr2")         #rmtree=remove tree

#Note: file/file/file ko sb ko delete kar deta hai.
#------
