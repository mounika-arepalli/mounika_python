Num=int(input("Enter the Integer:"))
#condition to check wheather the given integer is a three digit number or not
if((Num>=100 and Num<=999) or (Num>=-999 and Num<=-100)):
    print("Three digit number")
else:
    print("not a three digit number")