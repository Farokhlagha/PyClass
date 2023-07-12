import random

computer_number = random.randint(10,40)

for i in range(5):
    user_number = int(input())


    if computer_number == user_number:
        print("You win")
        print("✅")
        break

    elif computer_number > user_number:
        print("go up")
        print("⬆️")

    elif computer_number < user_number:
        print("go down")
        print("⬇️")
