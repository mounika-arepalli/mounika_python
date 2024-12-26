num1=int(input("enter the integer 1:"))
num2=int(input("enter the integer 2:"))
if(num1==num2):
    print("both are equal")
else:
    print("both are not equal")
#by using the ternary opeartor
print("-----------------------------------------------------------")
result="both are equal" if(num1==num2) else "both are not equal"
print(result)