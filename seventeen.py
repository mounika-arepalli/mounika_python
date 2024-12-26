num1=int(input("enter the integer 1:"))
num2=int(input("enter the integer 2:"))
num3=int(input("enter the integer 3:"))
if((num1<num2 and num1<num3) or (num1<num3 and num1<num2)):
    print(num1,"is smallest number")
elif((num2<num1 and num2<num3) or (num2<num3 and num2<num1)):
    print(num2,"is smallest number")
else:
    print(num3,"is smallest number")
