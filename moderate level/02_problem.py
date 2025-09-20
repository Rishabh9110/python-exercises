#Find the sum of numbers from 1 to n (user enters n).
n=int(input("enter the value of n:"))
i=0
sum=0
while(i<=n):
    sum=sum+i
    i=i+1
print(f"the sum upto {n} is:",sum)    