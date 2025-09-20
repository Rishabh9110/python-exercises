#Check if a given string is a palindrome.
num=int(input("enter the number to check if its palindrome or not:"))
number=num
reverse_number=0
digit=0
while(num>0):
    digit=num%10
    reverse_number=reverse_number*10+digit
    num=num//10
if(reverse_number==number)  :
    print(f"{number} is palindrome")
else:
    print(f"{number} is not palindrome")


    