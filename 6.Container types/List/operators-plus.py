x=[10,20,30,40]
y=[60,50,80,90]
z=x+y
print(z)        #1. airthmetic 2. concadination, 3. list merge

#x.append(y)
#print(x)        #[10, 20, 30, 40, [60, 50, 80, 90]]

x.extend(y)
print(x)
