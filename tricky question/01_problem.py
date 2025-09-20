#Create a “Number Guessing Game” (computer picks a random number, user guesses until correct).


# we are using random module which helps in generating random numbers or random choices
import random
number=random.randint(1,100)
guess=False
while guess==False:
    num=int(input("guess the number:"))
    if(num==number):
        print("conratulation you guessed the right number")
    elif(num<number):
        print("too low try again")  
    elif(num>number):
        print("too high try again")  
       


