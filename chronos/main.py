import time
import string
import random


def rando_str():
    letters = string.ascii_lowercase
    str_result = ( ''.join(random.choice(letters) for i in range(10)) )
    print("{}:{}".format(str_result, time.time()))
    
while True:
    rando_str()
    time.sleep(.1)
    