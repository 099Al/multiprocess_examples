#!/usr/bin/python

from multiprocessing import Process, Queue
import time
import random

def square(idx, x, queue):

    time.sleep(random.randint(1, 3))
    queue.put((idx, x * x))


def main():

    data = [2, 4, 6, 3, 5, 8, 9, 11]
    queue = Queue()
    processes = [Process(target=square, args=(idx, val, queue)) for idx, val in enumerate(data)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    unsorted_result = [queue.get() for _ in processes]

    result = [val[1] for val in sorted(unsorted_result)]
    print(result)


if __name__ == '__main__':
    main()