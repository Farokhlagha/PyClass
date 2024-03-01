import random

user_score = 0
computer_score = 0

while computer_score < 2 and user_score < 2:
    x = random.randint(1,3)

    if x == 1:
        computer_choice = "rock"
    elif x == 2:
        computer_choice ="paper"
    elif x == 3:
        computer_choice = "scissors"

    user_choice = input()
    print("🖥️: ", computer_choice)
    print("😊: ", user_choice)

    if computer_choice == "rock" and user_choice =="paper":
        user_score += 1

    elif computer_choice == "rock" and user_choice == "scissors":
        computer_score += 1  

    elif computer_choice == "paper" and user_choice == "rock":
        computer_score += 1 

    elif computer_choice == "paper" and user_choice == "scissors":
        user_score += 1

    elif computer_choice == "scissors" and user_choice == "paper":
        computer_score += 1

    elif computer_choice == "scissors" and user_choice == "rock":
        user_score += 1


