"""
Через Pool можно сделать общюю переменную след образом.
Создать функцию, которую использовать при инициализации Pool.
Тогда global Переменная в ней будет общей для дочерних процессов.
Переменная должна быть типа очередь, чтобы из нее можно было взять значение
"""
# example of sharing a global variable among all workers
import random
from time import sleep
from multiprocessing import SimpleQueue
from multiprocessing.pool import Pool


# initialize worker processes
def init_worker(shared_queue):
    # declare scope of a new global variable
    global queue
    # store argument in the global variable for this process
    queue = shared_queue


# task executed in a worker process
def task(identifier):
    # generate a value
    value = random.randint(1,5)
    # block for a moment
    sleep(value)
    # declare scope of shared queue
    global queue
    # send result using shared queue
    queue.put((identifier, value))


# protect the entry point
if __name__ == '__main__':
    # create a shared queue
    shared_queue = SimpleQueue()
    result = 0
    # create and configure the process pool
    with Pool(initializer=init_worker, initargs=(shared_queue,)) as pool:
        # issue tasks into the process pool
        _ = pool.map_async(task, range(10))
        # read results from the queue as they become available
        for i in range(10):
            out = shared_queue.get()
            prev_res = result
            result += out[1]
            print(f'item={out} {prev_res}+{out[1]}={result}', flush=True)