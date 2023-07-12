# SuperFastPython.com
# example of manually issuing a follow-up tasks to the process pool
from random import random
from time import sleep
from multiprocessing.pool import Pool


# task executed in a worker process
def task2(identifier, result):
    # generate a random number
    value = random()
    # block for a moment
    sleep(value)
    # report result
    print(f'>>{identifier} with {result}, generated {value}', flush=True)
    # return result
    return (identifier, result, value)


# task executed in a worker process
def task1(identifier):
    # generate a random number
    value = random()
    # block for a moment
    sleep(value)
    # report result
    print(f'>{identifier} generated {value}', flush=True)
    # return result
    return (identifier, value)


# protect the entry point
if __name__ == '__main__':
    # create and configure the process pool
    with Pool() as pool:
        # issue tasks to the process pool and process results
        for i, v in pool.imap_unordered(task1, range(10)):
            # check result
            if v > 0.5:
                # issue a follow-up task
                _ = pool.apply_async(task2, args=(i, v))
        # close the pool
        pool.close()
        # wait for all issued tasks to complete
        pool.join()
    # all done
    print('All done.')