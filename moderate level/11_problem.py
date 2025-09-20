#Make a countdown program using a while loop (start from user input and go to 1).
num=int(input("enter the value to start backward counting:"))
i=num
print(f"the backward counting form the {num} is:",end="")
while(i>=0):
    print(i,end=" ")
    i=i-1