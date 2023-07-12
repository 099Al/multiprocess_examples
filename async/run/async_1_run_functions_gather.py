import asyncio
from datetime import datetime
import random
import time

async def async_sleep(num):
    print(f"start async number: {num}")  #Эта часть выполняется сразу
    v=random.randint(1,7)
    await asyncio.sleep(v)     # Идет оставновка и переключение на другие задачи в event_loop
    #time.sleep(v)            #Так будет выполнение последовательно

    status = asyncio.all_tasks()
    resp = f"done number:{num} duration:{v}  {len(status)}"

    print(resp)
    with open('res.txt','a') as f:
        f.write(resp+'\n')

    return (num,)


async def main():
    start = datetime.now()

    coro_objs = []
    for i in range(1, 30):
        coro_objs.append(async_sleep(i))

    res = await asyncio.gather(*coro_objs)

    duration = datetime.now() - start
    print(f"Took {duration.total_seconds():.2f} seconds.")

    #Результат будут в порядке подачи параметров в List, т.к. запуск был через gather
    for t in res:
        print(t)

if __name__ == "__main__":
    with open('res.txt','w') as f:
        pass

    asyncio.run(main())