import threading
import numpy as np
import time
import random

def init_file():
    with open('latency.csv', 'w') as latf:
        latf.write('timestamp' + ',' + 'latency' + '\n')
    latf.close()

def gen_lat():
    threading.Timer(20, gen_lat).start()
    timestamp = int(time.time())
    latency = int(random.uniform(10, 20))
    with open('latency.csv','a') as latf:
        latf.write(str(timestamp) + ',' + str(latency) + '\n')
    print(timestamp, latency)


init_file()
gen_lat()
