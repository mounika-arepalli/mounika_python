num1=int(input("enter the integer 1:"))
num2=int(input("enter the integer 2:"))
if(num1>num2):
    print(num1,"is a greatest number")
else:
    print(num2,"is a greatest number")
#by using the ternary opeartor
print("-----------------------------------------------------------")
result="num1 is greater" if(num1>num2) else "num2 is greater"
print(result)