#Given a list of numbers, print the factorial of each element.
list=[]
for i in range(0,5):
    a=int(input("enter the number:"))
    list.append(a)
print(list)    
for j in list:
    fact=1
    for k in range(1,j+1):
        fact=fact*k
    print(f"Factorial of {j} is {fact}")
