import asyncio, random

async def download(code):
    wait_time = random.randint(1, 3)
    print('downloading {} will take {} second(s)'.format(code, wait_time))
    await asyncio.sleep(wait_time)  # I/O, context will switch to main function
    print('downloaded {}'.format(code))


async def download_worker(q):
    while True:
        code = await q.get()
        await download(code)
        q.task_done()

async def main():
    q = asyncio.Queue()
    workers = [asyncio.create_task(download_worker(q)) for _ in range(3)]
    i = 0


    while i < 9:
        await q.put(i)
        i += 1

    await q.join()  # wait for all tasks to be processed

    #for worker in workers:
    #    worker.cancel()
    #await asyncio.gather(*workers, return_exceptions=True)

if __name__ == '__main__':
    asyncio.run(main())