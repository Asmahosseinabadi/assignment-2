import random
high=0
low=0
win=0
computer_number=random.randint(10,40) #random number between 10 and 40
for i in range(10):
    user_number=int(input("enter your guess number:"))
    if computer_number==user_number:
        win+=1
        print("you win the game")
        print("🎉🎉🎉")  
        print("the number of guess is:",low+high+win)
        break
    elif computer_number<user_number:
        high+=1
        print("your guess is  high😥,guess a lower number")

    elif computer_number>user_number:
        low+=1
        print("yor guess is low🙄,guess a higher number")

else:
    print("-----------------------------------------")
    print("Gameeee Overrrr!!!!!!😓")
    

