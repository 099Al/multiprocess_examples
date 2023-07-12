# SuperFastPython.com
# example of submitting follow-up tasks to the process pool
from time import sleep
from random import random
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import as_completed


# test that works for moment
def task1():
    value = random()
    sleep(value)
    print(f'Task 1: {value}')
    return value


# test that works for moment
def task2(value1):
    value2 = random()
    sleep(value2)
    print(f'Task 2: value1={value1}, value2={value2}')
    return value2


# entry point
if __name__ == '__main__':
    # start the process pool
    with ProcessPoolExecutor(5) as executor:
        # send in the first tasks
        futures1 = [executor.submit(task1) for _ in range(10)]
        # process results in the order they are completed
        for future1 in as_completed(futures1):
            # get the result
            result = future1.result()
            # check if we should trigger a follow-up task
            if result > 0.5:
                _ = executor.submit(task2, result)
        # wait for all follow-up tasks to complete