year=int(input("enter the year:"))
if(year%400==0)and(year%100==0):
    print("year is a leap year",year)
elif(year%4==0)and(year%100!=0):
    print("year is a leap year",year)
else:
    print("year is not a leap year",year)