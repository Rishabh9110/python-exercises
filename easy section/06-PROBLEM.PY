#Take three numbers and print the largest.
num1=int(input("enter the value of num1:"))
num2=int(input("enter the value of num2:"))
num3=int(input("enter the value of num3:"))
if(num1>num2 and num1>num3):
    print("the greatest number is:",num1)
if(num2>num3 and num2>num1):
    print("the greatest number is:",num2)
else:
    print("the greatest number is:",num3)