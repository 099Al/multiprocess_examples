import asyncio
import random
import time
import datetime
from multiprocessing import Pool, Process, current_process, Manager


async def test_connect(p):
    t = random.randint(1,7)
    await asyncio.sleep(t)  #если использовать time.sleep(), то будет последовательное выполнение
    return t

async def scan(nm):
    print(f'start n:{nm}')
    res = await test_connect(nm)
    print(f'end n:{nm} wait:{res}')

async def main(l_param):
    tasks = [scan(x) for x in l_param]
    await asyncio.gather(*tasks)




def chunk_list(lst,s):
    new_l = []
    for x in range(0, len(lst), s):
        el = lst[x:x + s]
        new_l.append(el)
    return new_l


def pool_task(prm):
    for x in prm:

        process = current_process().name

        if process in dG:
            dG[process] = dG[process]+1
        else:
            dG[process]=1
        cnt = dG[process]

        start = datetime.datetime.now()

        print(process, x, prm, start.strftime('%H:%M:%S'))
        #time.sleep(random.randint(0, 5))
        time.sleep(1)
        end = datetime.datetime.now()
        s = start.strftime('%H:%M:%S')
        e = end.strftime('%H:%M:%S')
        dur = (end-start)
        out=f'{process} {x}---cnt={cnt} s:{s} e: {e} dur:{end-start}'
        print(out)


def init(d):
    global dG
    dG = d


if __name__ == '__main__':
    print('---start--')



    #l_rn = range(0,5)
    #l_rn = [chr(x) for x in range(65,95)]
    l_rn = [str(x) for x in range(1,50)]
    l_chs = chunk_list(l_rn,5)
    start_tm = datetime.datetime.now()

    d = Manager().dict()



    with Pool(5,initializer=init,initargs=(d,)) as pool:
        pool.map(pool_task,l_chs)

    #asyncio.run(main(l_rn))

    end_tm = datetime.datetime.now()

    print('total:',end_tm-start_tm)

    #test_connect('a')

    print('---end---')