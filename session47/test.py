# Example tqdm
from tqdm import tqdm
import time

for i in tqdm(range(100)):
    x = 1+3
    time.sleep(0.1)


#------------------
boys = ['ali', 'fsdfd', 'ddff', 'tyy']
girls = ['df', 'iio', 'ere', 'trtr']

for boy, girl in zip(boys, girls):
    print(boy, girl)



# ---------
a =2
b= 3
raise Exception('Error')
c= 4
d= 5
