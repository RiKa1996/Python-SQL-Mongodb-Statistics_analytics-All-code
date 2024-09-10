import random      #ye module ek luckey draw jaise kisi ek no ko chunta hai.
print(random.randint(1,100))  #1 se 100 tak me kisi ek no. ko hi chunega.
print(random.randint(1000,9999))   #ye otp nikanle ke liye kiya jata hai.
print(random.uniform(1,100))       #uniform function float value nikalne ke liye hota hai.
x=[10,20,30,40,50,60,70,10,50]
print(x)
print(random.shuffle(x))      #shuffle function hume None value wapas karta hai. #shuffle= tash ki gaddi jaise shuffle ki jati hai.
print(x)                           #but after shuffle x print() karne per sari value shuffle ho jati hai.
print(random.choice(x))       #choice function jo humpe x variable hai. usme se hume koi ek value choice kar ke dega
print(random.choice("Ducat india"))
y=random.sample(x,k=3)        #sample function hum jitni value mangna hai. wo utni hi value hume dega. exp: (x,k=3)
print(y)
z=x.copy()
print(z)
