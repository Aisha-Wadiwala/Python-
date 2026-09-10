# NUMBER GUESSING GAME
import random
print("==NUMBER GUESSING GAME==")

num = random.randint(1,100)
attempt = 0 
while True:
 choice = int(input("Enter Number:"))
 if(choice==num):
    print("CORRECT!")
    break
 elif(choice>num):
    print("TOO HIGH")
    attempt+=1
 elif(choice<num):
    print("TOO LOW")
    attempt+=1
 else:
    print("NOT CORRECT!")
print("Number of attempts are:",attempt+1)
