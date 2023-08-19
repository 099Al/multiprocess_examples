import asyncio
import time
import random

async def producer(x, q, semaphore):
    async with semaphore:
        print(f'start task {x}')
        w_t = random.randint(1,5)
        await asyncio.sleep(w_t)
        print(f'stop task {x}, time {w_t}')

        res = ('done',x)
        await q.put(res)


async def progress(q):
    cnt = 0
    while True:
        res = await q.get()
        if res == 'stop':
            print('DONE')
            break
        cnt = cnt + 1
        print(f'cnt:{cnt}')

async def main(l_t):

    q = asyncio.Queue()

    semaphore = asyncio.Semaphore(10)

    #----Вариант запуска 1--------
    tasks = [producer(t,q,semaphore) for t in l_t]
    progress_task = asyncio.create_task(progress(q))

    await asyncio.gather(*tasks)
    #_ = await asyncio.wait(tasks) #depricated
    await q.put('stop')
    await progress_task   #это не обязательно, т.к. progress_task все равно стартует
    #------------------------------------------


    # #---------------
    # #Вариант запуска 2
    # tasks = [producer(t, q, semaphore) for t in l_t]
    # tasks.append(progress(q))
    #
    # await asyncio.gather(*tasks)
    # await q.put('stop')
    # #-------------------------


if __name__ == '__main__':

    l_task = list(range(0,20))

    asyncio.run(main(l_task))