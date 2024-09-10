#time module
import time
print(time.ctime())    #ctime function jo bhi present timeing ho rhi hogi wo hume de dega

print(time.sleep(5))   #None value dega  #sleep function hume jitne sec hum sleep function me likhege wo hume utne sec ke liye rok dega.
print("bye")

# for loop laga ke
#=================
for i in range(1,11):
    time.sleep(1)
    print(i*5)
