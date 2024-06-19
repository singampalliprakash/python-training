marks=float(input("enter the marks:"))
if(0<marks<100):
    if(marks>=95):
        print("A+")
    elif(95>marks>=90):
        print("A grade")
    elif(90>marks>=80):
        print("B grade")
    elif(80>marks>=70):
        print("C grade")
    elif(70>marks>=60):
        print("D grade")
    elif(60>marks>=50):
        print("E grade")
    elif(marks<50):
        print("fail")
else:
    print("invalid marks")
print("marks%",marks)