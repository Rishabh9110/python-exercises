#Find the largest and smallest element in a list without using built-in functions.
list=[]
for i in range(0,5):
    a=int(input("enter the number:"))
    list.append(a)
smallest=list[0]
largest=list[0]
for j in list:
   if(j<smallest):
       smallest=j
for k in list:
    if(k>largest):
        largest=k

print(smallest)     
print(largest)