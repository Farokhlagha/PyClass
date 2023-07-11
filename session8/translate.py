

def read_from_file():
    f = open("session8/translate.txt", "r")

    # words = []
    # for line in f:
    #     words.append(line)

    temp = f.read().split("\n")

    words =[]
    for i in range(0, len(temp), 2):
        my_dict = {"en": temp[i], "fa": temp[i+1]}
        words.append(my_dict)

    f.close()

  #  print(words)
# words = [
#     {"en": "apple", "fa": "sib"},
#     {"en": "tree", "fa": "derakht"},
#     {"en": "one", "fa": "yek"}
# ]

read_from_file()
user_text = input("enter your english text: ")
user_words = user_text.split(" ")
print(user_words)


