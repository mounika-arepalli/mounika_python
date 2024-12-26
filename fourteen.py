num1=int(input("enter the integer 1:"))
num2=int(input("enter the integer 2:"))
if(num1<num2):
    print(num1,"is a smallest number")
else:
    print(num2,"is a smallest number")
#by using the ternary opeartor
print("-----------------------------------------------------------")
result="num1 is smallest" if(num1<num2) else "num2 is smallest"
print(result)