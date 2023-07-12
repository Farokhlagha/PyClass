import time

for i in range(3):
    password = input()
    if password == "1234":
        print("successful")
        print("welcom")
        break
    else:
        print("wrong password")
    
time.sleep(30)