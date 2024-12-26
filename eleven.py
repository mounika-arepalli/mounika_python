num=int(input("enter the integer:"))
if(num%3==0 and num%5==0):
    print(num,"is a multiple of 3 and 5")
else:
    print(num,"is not a multiple of 3 and 5")
# by using the ternary operator
print("------------------------------------")
result="is a multiple" if(num%3==0 and num%5==0) else "not a multiple"
print(result)
