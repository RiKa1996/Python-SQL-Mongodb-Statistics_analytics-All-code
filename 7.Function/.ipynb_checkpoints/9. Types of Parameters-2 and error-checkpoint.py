#Variable length Positional only
#===============================
def show(*a):              # a parameters ke prefix me stract(*) lagane per wo variable length positional only ban jata hai.
    print(a)               # aur ye hume ke tuple() me rakh kar milega

show()
show(12)
show(15,56,)
show(56,98,78)
show(32.23,25,36.45)

print("----------------------------------------------------------------")
#Variable length Keyword only

def show(**a):              # a parameters ke sufix me double stract(**) lagane per wo variable length keyword only ban jata hai.
    print(a)               # aur ye hume ke dictionery{} me rakh kar milega

show()
show(a=12)
show(a=15,b=56,)
show(b=56,a=98,x=78)
show(x=32.23,u=25,z=36.45)
print("----------------------------------------------------------------")

#dono ko mix kar ke dekhne per
def show(*a,**b):
    print(a)
    print(b)

show(56,69,88,777,225,a=663,b=4577,h=555,n=888)

#(56, 69, 88, 777, 225)
{'a': 663, 'b': 4577, 'h': 555, 'n': 888}

