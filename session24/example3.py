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

for url in urls:
    scrapper(url)

    
end_time = time.time()

print(end_time - start_time)