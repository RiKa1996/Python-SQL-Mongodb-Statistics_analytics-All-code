#Count method
s="india is a country"
print(s.count('u'))
print(s.count("z"))
print("--------------------------------------------------")
#startwith method
mob="123+91455498"
print("+91" in mob)   #in operator #true

print(mob.startswith("98"))  #false
print(mob.startswith("+91")) #false
print(mob.startswith("123")) #true

print("--------------------------------------------------")
#endstwith method
img="abc.jpg"
print(img.endswith("png"))
print(img.endswith("jpg"))

print("--------------------------------------------------")
#replace method
i="india"
print(i)
print(i.replace("i","I")) #old,new,all_replacements
print(i.replace("i","I",1)) #old,new,1_replacements #1 lagane se kewal aage ka chr bada hoga
