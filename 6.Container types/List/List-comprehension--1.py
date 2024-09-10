#List comprehension-->quick way to create list(in line expression)
#var=[expression for]

x=[i*j for i in range(1,5) for j in range(2,5)]
print(x)                


for i in range(1,5):
    for j in range(2,5):
        x.append(i*j)
print(x)

#1. list ko banane ke hum for loop ke sath jana jahte hai.
#2. for loop ke sath hum ek expression chalana jahte hai.
#3. us expression ke result ko hum append karna chahte hai.

#Note:jab ye teeno baate milegi jab hum comprehension use karna chaiye
