# from threading import Thread
from multiprocessing import Process
from time import time
import requests

def download(url, name):
    result = requests.get(url)

    f = open(name, 'wb')
    f.write(result.content)
    f.close()


urls = [
    ['https://picsum.photos/id/237/200/300', 'output/image1.jpg'],
    ['https://picsum.photos/seed/picsum/536/354', 'output/image2.jpg'],
    ['https://picsum.photos/id/1084/536/354?grayscale', 'output/image3.jpg' ], 
    ['https://picsum.photos/id/1060/536/354?blur=2', 'output/image4.jpg'],
    ['https://picsum.photos/id/870/536/354?grayscale&blur=2', 'output/image5.jpg'],
    ['https://picsum.photos/id/237/200/300', 'output/image6.jpg'],
    ['https://picsum.photos/seed/picsum/536/354', 'output/image7.jpg'],
    ['https://picsum.photos/id/1084/536/354?grayscale', 'output/image8.jpg' ], 
    ['https://picsum.photos/id/1060/536/354?blur=2', 'output/image9.jpg'],
    ['https://picsum.photos/id/870/536/354?grayscale&blur=2', 'output/image10.jpg']
]

start_time = time()

threads = []
for url, name in urls:
    threads.append(Process(target=download, args=[url, name]))

for t in threads:
    t.start()

for t in threads:
    t.join()

end_time = time()

print(end_time - start_time)