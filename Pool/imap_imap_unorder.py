import multiprocessing
import time

def func(x):
    time.sleep(x)
    return x + 2

if __name__ == "__main__":
    p = multiprocessing.Pool()
    start = time.time()
    for x in p.imap_unordered(func, [1,5,3]):
        print("{} (Time elapsed: {}s)".format(x, int(time.time() - start)))