# SuperFastPython.com
# example of a simple progress indicator for tasks in a process pool
from time import sleep
from random import random
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import wait


# simple progress indicator callback function
def progress_indicator(future):
    print('.', end='', flush=True)


# mock test that works for moment
def task(name):
    sleep(random())


# entry point
if __name__ == '__main__':
    # start the process pool
    with ProcessPoolExecutor(2) as executor:
        # send in the tasks
        futures = [executor.submit(task, i) for i in range(20)]
        # register the progress indicator callback
        for future in futures:
            future.add_done_callback(progress_indicator)
        # wait for all tasks to complete
    print('\nDone!')