w=int(input("enter the weight of watermelon:"))
if(w%2!=0):
 print("no it is odd")
else:
    x=w/2
    if(x%2==0):
      print("yes,brother 1 gets",int(x),"brother 2 gets",int(x))
    else:
        print("yes,brother1 gets",int(x-1),"brother2 gets",int(x+1))