#Take a list as input and check if it has duplicate elements.
list=[]
item=int(input("enter the items no present in list:"))

for i in range(0,item):
    n=int(input("enter the numbers:"))
    list.append(n)
     
print(list)
found= False
for j in range(0,len(list)):
    for k in range(j+1,len(list)):
        if(list[j]==list[k]):
            found=True
            break
    if found:
        break
       
if found:
    print("duplicate item is found")
else:
    print("duplicate item is not found")
        

       
           
          
       