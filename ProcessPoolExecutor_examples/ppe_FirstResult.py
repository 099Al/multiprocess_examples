# SuperFastPython.com
# example of waiting for the first result
from time import sleep
from random import random
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import wait
from concurrent.futures import FIRST_COMPLETED


# custom task that will sleep for a variable amount of time
def task(name):
    # sleep for less than a second
    value = random()
    sleep(value * 10)
    return f'Task={name}: {value:.2f}'


# entry point
if __name__ == '__main__':
    # start the process pool
    with ProcessPoolExecutor(10) as executor:
        # submit tasks and collect futures
        futures = [executor.submit(task, i) for i in range(10)]
        # wait until any task completes
        done, not_done = wait(futures, return_when=FIRST_COMPLETED)
        # get the future from the done set
        future = done.pop()
        # get the result from the first task to complete
        result = future.result()
        print(result)