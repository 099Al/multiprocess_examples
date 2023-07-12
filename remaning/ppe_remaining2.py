# SuperFastPython.com
# example of estimating the number of remaining tasks
from time import sleep
from random import random
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import as_completed


# mock test that works for moment
def task():
    value = random()
    sleep(value)


# entry point
def main():
    # start the process pool
    with ProcessPoolExecutor(4) as executor:
        # submit many tasks
        futures = [executor.submit(task) for _ in range(50)]
        print('Waiting for tasks to complete...')
        # update each time a task finishes
        for _ in as_completed(futures):
            # report the number of remaining tasks
            print(f'About {len(executor._pending_work_items)} tasks remain')


if __name__ == '__main__':
    main()