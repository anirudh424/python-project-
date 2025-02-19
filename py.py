import random

computer = random.choice([-1,0,1])
uc = input("Enter your choice: ")
dic = {"s": 1, "w" : -1, "g" : 0}
rev = {1 : "Snake", -1 : "Water", 0 : "Gun"}

you = dic[uc]

print(f"you chose {you} \ncomputer choice {rev[computer]}")


if(computer==you):
    print("IT'S A DRAW, TRY ONCE MORE")
    
else:
    if(computer==-1 and you==1):
        print("you win")
    elif(computer==-1 and you==0):
        print("you lose")
    elif(computer==1 and you==-1):
        print("you lose")
    elif(computer==1 and you==0):
        print("you win")
    elif(computer==0 and you==-1):
        print("you win")
    elif(computer==0 and you==1):
        print("you lose")
        
    else:
        print("SOMETHING WENT WRONG")
