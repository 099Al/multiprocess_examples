from multiprocessing import Pool, TimeoutError
import time
import os

def f(x):
    return x*x

if __name__ == '__main__':
    # запуск 4 рабочих процессов
    with Pool(processes=4) as pool:

        # печать "[0, 1, 4,..., 81]"
        print(pool.map(f, range(10)))

        # печатать одинаковые числа в произвольном порядке
        for i in pool.imap_unordered(f, range(10)):
            print(i)

        # вычислить "f(20)" асинхронно
        res = pool.apply_async(f, (20,))      # запускается в *только* одном процессе
        print(res.get(timeout=1))             # печатает "400"

        # вычислить "os.getpid()" асинхронно
        res = pool.apply_async(os.getpid, ()) # запускается в *только* одном процессе
        print(res.get(timeout=1))             # печатает PID этого процесса

        # запуск нескольких оценок асинхронно *может* использовать больше процессов
        multiple_results = [pool.apply_async(os.getpid, ()) for i in range(4)]
        print([res.get(timeout=1) for res in multiple_results])

        # уснуть одному рабочему на 10 секунд
        res = pool.apply_async(time.sleep, (10,))
        try:
            print(res.get(timeout=1))
        except TimeoutError:
            print("We lacked patience and got a multiprocessing.TimeoutError")

        print("For the moment, the pool remains available for more work")

    # выход из блока with с остановкой пула
    print("Now the pool is closed and no longer available")