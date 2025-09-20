#Count the number of vowels and consonants in a sentence.
sen=input("enter the sentence:")
vowels=0
consonent=0
for j in sen:
    sen=sen.lower()
    if(j=="a" or j=="e" or j=="i" or j=="o" or j=="u"):
        
        vowels=vowels+1
    elif(j>="a" and j<="z"):
        
        consonent=consonent+1
print("vowels:",vowels)
print("consonent:",consonent)