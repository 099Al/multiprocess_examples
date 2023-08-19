import asyncio
from multiprocessing import Pool, Process, current_process, Manager
import random
import time
import datetime


#src_data = [chr(x) for x in range(65,90)]
data = [(x,) for x in range(1,30)]

#src_data = [1,2,3]

def init(lock,d_task,q):
    global lG
    global dG
    global qG
    lG = lock
    dG = d_task
    qG = q
async def utask_a(p):
    v = random.randint(0,10)
    process = current_process().name

    if process not in dG:
        dG[process]=1
    else:
        dG[process]=dG[process]+1
    cnt = dG[process]

    qG.get()
    q_cnt = qG.qsize()

    start = datetime.datetime.now().strftime('%M:%S')
    with lG:
        print(p, process, cnt, start,f'q={q_cnt}')
    await asyncio.sleep(v)
    end = datetime.datetime.now().strftime('%M:%S')
    with lG:
        print(p,process,cnt,start,end,v)

def utask(p):
    v = random.randint(0,5)
    process = current_process().name
    start = datetime.datetime.now().strftime('%M:%S')
    print(p, process, start)
    time.sleep(v)
    end = datetime.datetime.now().strftime('%M :%S')
    with lG:
        print(str(p), process, start, end , v)

def wrapper(p):
    asyncio.get_event_loop().run_until_complete(utask_a(p))



if __name__ == '__main__':
    print(data)

    manager = Manager()
    lock = manager.Lock()
    d_task=manager.dict()
    queue = manager.Queue()

    #Для подсчета оставшихся элементов
    for x in data:
        queue.put(1)



    #lock = asyncio.Lock

    cnt=0



    with Pool(6, initializer=init, initargs=(lock,d_task,queue), maxtasksperchild=4) as pool:
        pool.starmap(wrapper,data)


    #with Pool(3,initializer=init, initargs=(lock,),  maxtasksperchild=2) as pool:
    #    pool.starmap(utask,src_data)


