# SuperFastPython.com
# benchmark memory usage of creating threads
import time
import threading
import tracemalloc


# task to run in a new thread
def task():
    for i in range(10):
        # block for a moment
        time.sleep(0.1)


# benchmark running a given number of threads threads
def benchmark(n_threads):
    # record memory usage
    tracemalloc.start()
    # create many threads
    tasks = [threading.Thread(target=task) for _ in range(n_threads)]
    # start many threads
    for thread in tasks:
        thread.start()
    # wait a moment
    time.sleep(0.5)
    # take a snapshot while all threads are running
    snapshot = tracemalloc.take_snapshot()
    # wait for all threads to finish
    for thread in tasks:
        thread.join()


    # calculate total memory usage
    total_bytes = sum(stat.size for stat in snapshot.statistics('lineno'))
    # convert to kb
    total_kb = total_bytes / 1024.0
    # return memory usage
    return total_kb

if __name__ == '__main__':

    # define number of threads to test creating
    n_benchmark = [1, 10, 100, 1000, 2000, 5000, 10000]
    # benchmark running different numbers of threads
    for n in n_benchmark:
        # perform benchmark
        total_kb = benchmark(n)
        # report result
        print(f'> threads={n:5} used {total_kb:.3f} KiB')