import os

# result = os.listdir("session2")
# print(result)


# pip install imageio
import imageio

file_list = sorted(os.listdir("session8/images"))

IMAGE = []
for file_name in file_list:
    file_path = "session8/images/" + file_name # / after images
    image = imageio.imread(file_path)
    IMAGE.append(image)


imageio.mimsave("session8/my_output.gif", IMAGE) 
