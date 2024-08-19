import random
n =random.randint(1,100) # random integer generate 
a=-1
guesses=1
while(a!=n): # n kabhi -1 nhi ho ga to ya condition while wali hamsha rahy gi
    a=int(input("Enter the number: "))
    
    if(a>n):
        print("Lower number please")
        guesses+=1
    elif(a<n):
        print("Higher number please")
        guesses+=1 
        
        
print(f"  You have guessed the number {n} correctly in {guesses} attempts")