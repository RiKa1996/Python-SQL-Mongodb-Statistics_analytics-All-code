#parallel iterations
roll=[10,11,12]
name=["rishav","gulshan","aryan","anil"]

for i in zip(roll,name):
    print(i)

for (r,n) in zip(roll,name):
    print(r,n)
    
print("----------------------------------------------------------")
#Note:jo sbse choti line ka container hoga use hi kiya jata hai.
#----------------------------------------------------------------
roll=[10,11,12]
name=["rishav","gulshan","aryan"]

for i in zip(roll,name):
    print(i)

for (r,n) in zip(roll,name):
    print(r,n)
    
print('----------------------------------------------------------')
roll=[10,11,12]
name=["rishav","gulshan","aryan"]

for tup in zip(roll,name):     #tuple ka use karke tuple me la skte hai.
    print(tup)
    
print('----------------------------------------------------------')
roll=[10,11,12]
name=["rishav","gulshan","aryan"]
marks=[60,80,67,90]
for r,n,m in zip(roll,name,marks): #seprate krke bhi kar skte hai.
    print(r,n,m)
