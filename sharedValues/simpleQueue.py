"""
SimpleQueue is always unbounded, unlike Queue that can be configured to be bounded or unbounded.
SimpleQueue does not offer qsize() or full() functions.
SimpleQueue does not offer “block” or “timeout” arguments on get() and put().
SimpleQueue does not offer put_nowait() and get_nowait() functions.
SimpleQueue does not offer join_thread() and cancel_join_thread() functions.

This minimal interface includes:

Close the queue and release resources via close().
Check if empty via empty().
Add an item to the queue via put().
Get an item from the queue via get().

"""
from time import sleep
from random import random,randint
from multiprocessing import Process
from multiprocessing import SimpleQueue


# generate work
def producer(queue):
    print('Producer: Running', flush=True)
    # generate work
    for i in range(10):
        # generate a value
        value = randint(1,10)
        # block
        sleep(value/10)
        # add to the queue
        queue.put(value)
    # all done
    queue.put(None)
    print('Producer: Done', flush=True)


# consume work
def consumer(queue):
    print('Consumer: Running', flush=True)
    # consume work
    while True:
        # get a unit of work
        item = queue.get()
        # check for stop
        if item is None:
            break
        # report
        print(f'>got {item}', flush=True)
    # all done
    print('Consumer: Done', flush=True)


# entry point
if __name__ == '__main__':
    # create the shared queue
    queue = SimpleQueue()
    # start the consumer
    consumer_process = Process(target=consumer, args=(queue,))
    consumer_process.start()
    # start the producer
    producer_process = Process(target=producer, args=(queue,))
    producer_process.start()
    # wait for all child processes to finish
    producer_process.join()
    consumer_process.join()

    print('-----')