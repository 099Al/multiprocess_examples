# SuperFastPython.com
# example of reporting the number of remaining tasks with apply_async()
from time import sleep
from random import random
from multiprocessing.pool import Pool


# task executed in a worker process
def task(i):
    # block for a fraction of a second
    sleep(random())


# protect the entry point
if __name__ == '__main__':
    # create the pool
    with Pool() as pool:
        # issue many tasks
        results = [pool.apply_async(task,'a') for _ in range(50)]
        # report remaining tasks for a while
        count = len(results)

        while count:
            # check all tasks and count the number that are not done
            count = sum([not r.ready() for r in results])
            # report the number of remaining tasks
            print(f'>{count}/{len(results)} tasks remain')
            # wait a moment
            sleep(0.5)