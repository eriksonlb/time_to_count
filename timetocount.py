from time import time
from datetime import datetime 

t1 = time()


for i in range(1000):
    ...

t2 = time()

print(t2 - t1)

def timeit(func):
    def inner(*args, **kwargs):
        start_time = datetime.now() 
        state = func(*args, **kwargs)
        time_elapsed = datetime.now() - start_time 
        print('Time elapsed : {} :(hh:mm:ss.ms) {}'.format(func.__name__, time_elapsed))
        return state
    return inner

@timeit
def soma_1(x):
    for x in range(1000000000000):
        print(x)
    return x + 1

@timeit
def soma_2(x):
    return x + 2


