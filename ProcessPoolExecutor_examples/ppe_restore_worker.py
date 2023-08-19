# SuperFastPython.com
# example of retrying a failed task a second time
from random import random
from time import sleep
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import as_completed


# task that sleeps for a moment and may fail with an exception
def work(identifier):
    # sleep for a moment
    sleep(random())
    # conditionally fail with a chance of 30%
    if random() < 0.3:
        raise Exception(f'Something bad happened {identifier}')
    return f'Completed {identifier}'


if __name__ == '__main__':
    # create a process pool
    with ProcessPoolExecutor(10) as executor:
        # submit ten tasks
        futures_to_data = {executor.submit(work, i): i for i in range(10)}
        # record of retried tasks
        retries = {}
        # process work as it completes
        for future in as_completed(futures_to_data):
            # check for a failure
            if future.exception():
                # get the associated src_data for the task
                data = futures_to_data[future]
                # submit the task again
                future = executor.submit(work, data)
                # store so we can track the retries
                retries[future] = data
                # report progress
                print(f'Failure, retrying {data}')
            else:
                # report successful result
                print(future.result())
        # wait for retries
        print('\nRetries:')
        for future in as_completed(retries):
            # check for a failure
            if future.exception():
                # get the associated src_data for the task
                data = retries[future]
                # failure
                print(f'Failure on retry: {data}, not trying again')
            else:
                # report successful result
                print(future.result())