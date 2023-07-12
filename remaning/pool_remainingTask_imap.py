# SuperFastPython.com
# example of reporting the number of remaining tasks with imap_unordered()
from time import sleep
from random import random
from multiprocessing.pool import Pool


# task executed in a worker process
def task(arg):
    # block for a fraction of a second
    sleep(random())


# protect the entry point
if __name__ == '__main__':
    # create the pool
    with Pool() as pool:
        # number of tasks
        n_tasks = 50
        # keep track of the number of tasks completed
        completed = 0
        step = 0
        # issue tasks and respond each time a task is completed
        for _ in pool.imap_unordered(task, range(50)):
            # updated completed tasks
            step += 1

            if step == 10:
                completed += step
                step =0
                # report the number of remaining tasks
                print(f'>{(n_tasks - completed)}/{n_tasks} tasks remain')