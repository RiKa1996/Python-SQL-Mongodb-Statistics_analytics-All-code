#List comprehension-->quick way to create list(in line expression)
#var=[expression for]

x=[2*3 for i in range(1,5)]
print(x)                    #[6, 6, 6, 6

x=[2*i for i in range(1,5)]
print(x)                    #[2, 4, 6, 8]

x=[i*i for i in range(1,5)]
print(x)                    #[1, 4, 9, 16]

x=[int(input("enter value:")) for i in range(1,5)]
print(x)
