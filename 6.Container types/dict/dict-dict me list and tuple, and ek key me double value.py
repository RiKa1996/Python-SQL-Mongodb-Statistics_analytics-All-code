#dict
d={}
print(type(d),d)

d={101:"sonu",500:"monu",201:"sonu",500:"chintu"}
print(d)        #ydi humari key double bar hai to jo humhari phli key hogi wo usme value phle print hogi.

d={'a':100,5.5:"hi",1:'apple'}   #{'a': 100, 5.5: 'hi', 1: 'apple'}
print(d)                         #dict me sabhi type ki key and value type ho skti hai.but humhara key same nhi hona chaiye


#ek key me double value ya usse jyada value ho skti hai.
ipl={"csk":['dhoni','raina'],'mi':('rohit','pandya')}   #aur ise list,tuple,set,frozenset,dict kisi me bhi likh skte hai.
print(ipl)

d={():'hi'} #dict me tuple aa skta hai kyoki tuple immutable hota hai.
print(d)

d={[]:'hi'} #dict me list nhi aa skta hai kyoki list mmutable hota hai.
print(d)
