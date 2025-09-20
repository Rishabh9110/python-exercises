#From a list, create a new list containing squares of all even numbers.
list=[20,30,45,60,23,90]
list1=[]
i=0
while(i<len(list)):
    if(list[i]%2==0):
       list1.append(list[i])
    i=i+1
print(list1)


