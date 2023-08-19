# SuperFastPython.com
# benchmark of starting coroutines
import tracemalloc
import asyncio


# task to run in a new thread
async def task():
    for i in range(10):
        # block for a moment
        await asyncio.sleep(0.1)


# benchmark running a given number of coroutines coroutines
async def benchmark(n_coros):
    # record memory usage
    tracemalloc.start()
    # create and schedule coroutines as tasks
    tasks = [asyncio.create_task(task()) for _ in range(n_coros)]
    # wait a moment
    await asyncio.sleep(0.5)
    # take a snapshot while all threads are running
    snapshot = tracemalloc.take_snapshot()
    # wait for all tasks to completes
    _ = await asyncio.wait(tasks)
    # calculate total memory usage
    total_bytes = sum(stat.size for stat in snapshot.statistics('lineno'))
    # convert to kb
    total_kb = total_bytes / 1024.0
    # return memory usage
    return total_kb


# main coroutine
async def main():
    # define numbers of coroutines to test creating
    n_benchmark = [1, 10, 100, 1000, 2000, 5000, 10000, 50000, 100000]
    # benchmark creating different numbers of coroutines
    for n in n_benchmark:
        # perform benchmark
        total_kb = await benchmark(n)
        # report result
        print(f'> coroutines={n:5} used {total_kb:.3f} KiB')

if __name__ == '__main__':

    # start the asyncio program
    asyncio.run(main())