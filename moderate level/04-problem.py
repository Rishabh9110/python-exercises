#Take 5 numbers from the user and print the maximum and minimum.
list=[]
for i in range(0,5):
    n=int(input("enter the number:"))
    list.append(n)
maximum=list[0]
minimum=list[0]
for num in list:
    if(num>maximum):
        maximum=num
for i in list:
    if(num<minimum):
        minimum=num
print("maximum no:",maximum)  
print("minimum no:",minimum)          

    

