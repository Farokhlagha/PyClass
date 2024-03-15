from threading import Thread
import time
import requests


start_time = time.time()

def scrapper(url):
    result = requests.get(url)
    print(result.text)


urls = ['https://google.com',
        'https://apple.com',
        'https://microsoft.com',
        'https://w3schools.com',
        'https://yahoo.com',
        'https://bing.com']

threads = []
for url in urls:
    new_thread = Thread(target=scrapper, args=[url])
    threads.append(new_thread)


for t in threads:
    t.start()

for t in threads:
    t.join()

end_time = time.time()

print(end_time - start_time)