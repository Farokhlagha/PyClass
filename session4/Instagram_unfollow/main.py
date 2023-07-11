import instaloader
import getpass


f = open("followers.txt","r")
old_followers = []
for line in f:
    old_followers.append(line)
f.close()

L = instaloader.Instaloader()

username = input("enter username: ")
password = getpass.getpass("enter password: ")

L.login(username, password)
print("Hoora, successfully login!")

profile = instaloader.Profile.from_username(L.context, "leylarazeghi")

new_followers = []
for follower in profile.get_followees():
    new_followers.append(follower)

    for old_follower in old_followers():
        if old_follower not in new_followers:
            print(old_follower)


f = open("followers.txt", "w")
for follower in new_followers:
    f.write(follower +"\n")
f.close()
        
