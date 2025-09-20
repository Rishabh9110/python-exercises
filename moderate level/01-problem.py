#Print the multiplication table of a number entered by the user.
num=int(input("enter the number:"))
for i in range(1,11):
    print(f"{num}x{i}={(num*i)}")