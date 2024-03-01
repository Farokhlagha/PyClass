import random
words_bank = ["tree", "book", "blue", "train", "woman"]
x= random.randint(0, len(words_bank)-1)
word = words_bank[x]
user_mistakes = 0
good_char = []
bad_char = []


while user_mistakes <6 :
    for i in range(len(word)):
        if word[i] in good_char:
             print(word[i],end=" ")
        else:
             print("- ", end=" ")

    if len(word) == len(good_char):
         print("you win!")
         break

    user_char = input("pls write your guess: ")
    if len(user_char) ==1:
        if user_char in word:
            good_char.append(user_char)
            print("✅")
        else:
                bad_char.append(user_char)
                user_mistakes +=1
                print("❌") 
    else:
         print("enter again!")

if user_mistakes == 6:
     print("game over!") 
           
