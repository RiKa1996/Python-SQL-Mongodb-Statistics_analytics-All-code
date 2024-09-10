#frozenset-->it is immutable version of set
#it is iterable

fs=frozenset()
print(type(fs),len(fs))

fs=frozenset([10,20,30,50,50,10,80,90])#list se[]
print(fs)                              #frozenset({10, 80, 50, 20, 90, 30})


fs=frozenset((10,20,30,50,50,10,80,90))#tuple se()
print(fs)                              #frozenset({10, 80, 50, 20, 90, 30})


fs=frozenset(range(50))          #range function se
print(fs)

for i in fs:
    print(i)
