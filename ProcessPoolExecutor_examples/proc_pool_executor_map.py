# SuperFastPython.com
# example of the map and wait pattern for the ProcessPoolExecutor
from time import sleep
from random import random,randint
from concurrent.futures import ProcessPoolExecutor
import concurrent.futures

# custom task that will sleep for a variable amount of time
def task(name):
    # sleep for less than a second
    r = randint(1,9)
    sleep(r)
    return name,r


# entry point
"""
map - выдает результат в том порядке, в котором task-и были поданы на вход
"""
if __name__ == '__main__':

    # start the process pool


    print('----map-------')
    with ProcessPoolExecutor(5) as executor:
        # execute tasks concurrently and process results in order
        for result in executor.map(task, range(10)):
            # retrieve the result
            print(result)

    print('----submit------')
    #Выдает результат сразу, как только появится
    with ProcessPoolExecutor(5) as executor:
        # execute tasks concurrently and process results in order
        futures = [executor.submit(task, i) for i in range(10)]
        for future in concurrent.futures.as_completed(futures):
            res = future.result()
            print(res)






