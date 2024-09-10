#.values method
d={101:"mango",102:"mango",103:"mango"}
print(d.values())             #dict_values(['mango', 'mango', 'mango'])

#keys method
d={101:"mango",102:"apple",103:"orange"}
print(d.keys())


#.items method
print(d.items())  #dict_items([(101, 'mango'), (102, 'apple'), (103, 'orange')])

for tup in d.items():   #with tuple
    print(tup)
print("----------------------")
for k,v in d.items():   #without tuple,list
    print(k,v)
