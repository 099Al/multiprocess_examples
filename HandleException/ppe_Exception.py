# SuperFastPython.com
# example of checking for an exception directly
from time import sleep
from concurrent.futures import ProcessPoolExecutor


# task that will block for a moment
def work():
    sleep(1)
    raise Exception('Something bad happened')
    return "Task is done"


# entry point
if __name__ == '__main__':
    # create a process pool
    with ProcessPoolExecutor() as executor:
        # execute our task
        future = executor.submit(work)
        # get the exception from the task when it is finished
        exception = future.exception()
        print(exception)