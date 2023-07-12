import asyncio
from multiprocessing import Pool, Process, current_process
from asyncio import current_task
import random
import time
import datetime


#data = [chr(x) for x in range(65,90)]
data = [(x,) for x in range(1,10)]

#data = [1,2,3]

async def utask_a(p):
    v = random.randint(0,10)
    start = datetime.datetime.now().strftime('%M:%S')
    process = current_process().name.replace('SpawnPool','')
    task = current_task().get_name()
    pid = current_process().pid
    log = f'{str(p)} {process}({pid}) {task} {start}  wait:{v}'
    print(log)
    await asyncio.sleep(v)
    end = datetime.datetime.now().strftime('%M:%S')
    log2 = f'{str(p)} {process}({pid}) {task} {start} {end} wait:{v}'
    print(log2)

def utask(p):
    v = random.randint(0,5)
    start = datetime.datetime.now().strftime('%M:%S')
    time.sleep(v)
    process = current_process().name.replace('SpawnPool','')
    pid  = current_process().pid
    task = current_task().get_name()
    end = datetime.datetime.now().strftime('%M :%S')
    log = f'{str(p)} {process}({pid}) {task} {start} {end} wait:{v}'
    print(log)

def wrapper(p):
    asyncio.get_event_loop().run_until_complete(utask_a(p))

if __name__ == '__main__':
    print(data)

    with Pool(4,maxtasksperchild=5) as pool:
        pool.starmap(wrapper,data)


