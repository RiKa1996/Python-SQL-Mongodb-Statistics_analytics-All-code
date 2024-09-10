marks=float(input("enter marks:"))
if (marks>=0 and marks<30):
    print("Fail")
elif(marks>=30 and marks<45):
    print("3rd division")
elif(marks>=45 and marks<60):
    print("2nd division")
elif(marks>=60 and marks<=100):
    print("1st division")
elif(marks>100 or marks<0):
    print("invalid marks")
print("bye")
