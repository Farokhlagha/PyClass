# f = open("session4\ketab.txt", "r")

# for line in f.readlines():
#     print(line)
# f.close()


# f = open("session4\ketab.txt", "a")
# f.write("salam bachehaaaa")
# f.close()


friends = ["ali","amir", "lili", "nazi","tara"]
f = open("session4\doost ha.txt", "w")

for friend in friends:
    f.write(friend)
    f.write("\n")
f.close()
