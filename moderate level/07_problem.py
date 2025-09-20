#Print the first n terms of the Fibonacci series.
num = int(input("Enter how many Fibonacci terms you want: "))

first = 0
second = 1

if num >= 1:
    print(first, end=" ")

if num >= 2:
    print(second, end=" ")

i = 3                # we already printed first two
while i <= num:
    third = first + second
    print(third, end=" ")
    first = second
    second = third
    i = i + 1
