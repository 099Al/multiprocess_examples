# SuperFastPython.com
# example of not flushing output when call print() from tasks in new processes
from time import sleep
from random import random
from multiprocessing import Pool


# custom function executed in another process
def task(value):
    # block for a moment
    sleep(3)
    # report a message
    #print(f'Done: {value}')
    print(f'Done: {value}',flush=True)


# protect the entry point
if __name__ == '__main__':
    # start the process pool
    with Pool() as pool:
        # submit all tasks
        pool.map(task, range(5))