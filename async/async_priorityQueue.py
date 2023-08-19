# SuperFastPython.com
# example of using the asyncio priority queue
from time import sleep
from random import random
from random import randint
import asyncio

#В очереди функции выполняются последовательно
# generate work
async def producer(queue):
    print('Producer: Running')
    # generate work
    for i in range(20):
        # generate a value
        value = round(random(),3)
        # generate a priority
        priority = randint(1, 10)     #1 - убрать приоритетность
        # create an item
        item = (priority, value,i)
        # add to the queue
        await queue.put(item)
    # wait for all items to be processed
    print('---1----')
    await queue.join() #Ожидание, когда все элементы обработаются. Освободятся из очереди
    print('---2---')
    # send sentinel value
    await queue.put(None)
    print('Producer: Done')


# consume work
async def consumer(queue):
    print('Consumer: Running')
    # consume work
    while True:
        # get a unit of work
        item = await queue.get()
        # check for stop
        if item is None:
            break
        # block
        await asyncio.sleep(item[1])
        # report
        print(f'>got {item} qsize={queue.qsize()}')
        # mark it as processed
        queue.task_done()
    # all done
    print('Consumer: Done')


# entry point coroutine
async def main():
    # create the shared queue
    queue = asyncio.PriorityQueue()
    # run the producer and consumers
    await asyncio.gather(producer(queue), consumer(queue))


# start the asyncio program
asyncio.run(main())