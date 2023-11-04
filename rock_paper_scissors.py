import random
computer_score=0
user_score=0
for i in range(6):
    option=random.randint(1,3)
    if option==1:
        computer_choice="rock"
    elif option==2:
        computer_choice="paper"
    elif option==3:
        computer_choice="scissors"

    user_choice=input("enter your choise:")

    print("💻",computer_choice)
    print("👤",user_choice)

    if computer_choice=="rock" and user_choice=="rock":
        print("choices are the same,no score!")
    elif computer_choice=="rock" and user_choice=="paper":
        user_score+=1
        print("one score for user")
    elif computer_choice=="rock" and user_choice=="scissors":
        computer_score+=1
        print("one score for computer")
    elif computer_choice=="paper" and user_choice=="paper":
        print("choices are the same,no score!")
    elif computer_choice=="paper" and user_choice=="rock":
        computer_score+=1
        print("one score for computer")
    elif computer_choice=="paper" and user_choice=="scissors":
        user_score+=1
        print("one score for user")
    elif computer_choice=="scissors" and user_choice=="scissors":
        print("choices are the same,no score!")
    elif computer_choice=="scissors" and user_choice=="paper":
        computer_score+=1
        print("one score for computer")
    elif computer_choice=="scissors" and user_choice=="rock":
        user_score+=1
        print("one score for user")
    
if computer_score>user_score:
    print("computer is the winner💻")
    print("the computer_score is: ",computer_score)
elif user_score>computer_score:
    print("user is the winner👤")
    print("the user_score is: ",user_score)
elif user_score==computer_score:
    print("the same score😁")


    

