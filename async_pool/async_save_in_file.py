import asyncio
import random
import time
import datetime
from multiprocessing import Pool, Process, current_process, Manager
import aiofiles
"""
Для каждого процесса записываются результат в отдельный файл.
НЕ ВСЕ записи успевают ЗАПИСАТЬСЯ!!!
блокировка через manager.Lock и asyncio.Lock Не работает

"""

async def test_connect(p):
    t = random.randint(1,7)
    #await asyncio.sleep(t)  #если использовать time.sleep(), то будет последовательное выполнение
    await asyncio.sleep(t)
    return t

async def scan(nm,list_prm):
    process = current_process().name.replace('SpawnPoolWorker','Process')
    tsk = asyncio.current_task().get_name()

    #---кол-во запусков процессов
    #--- Номер таска в одном процессе все время будет увеличиваться
    #--- Поэтому считаем только таски
    cnt = dG[process]





    start = datetime.datetime.now().strftime('%H:%M:%S')

    print(f'start n:{nm} process-task:{process}-{tsk} tasks:{list_prm}')
    log1 = f'STA {process}-{tsk} cnt={cnt} tasks:{list_prm} task_el=:{nm} start:{start} \n'

    async with aiofiles.open('pool_async_{}.txt'.format(process),'a+') as f:
        await f.write(log1)

    res = await test_connect(nm)

    end = datetime.datetime.now().strftime('%H:%M:%S')

    print(f'end {process}-{tsk} n:{nm} wait:{res}')
    log2 = f'END {process}-{tsk} cnt={cnt} tasks:{list_prm} task_el=:{nm} start:{start} end:{end} wait:{res}\n'

    async with aiofiles.open('pool_async_{}.txt'.format(process),'a+') as f:
        await f.write(log2)




async def main(l_param):
    tasks = [scan(x,l_param) for x in l_param]
    await asyncio.gather(*tasks)




def chunk_list(lst,s):
    new_l = []
    for x in range(0, len(lst), s):
        el = lst[x:x + s]
        new_l.append(el)
    return new_l


def pool_task(prm):

    process = current_process().name
    start = datetime.datetime.now()

    print(process, prm, start.strftime('%H:%M:%S'))
    # time.sleep(random.randint(0, 5))
    process = current_process().name.replace('SpawnPoolWorker','Process')


    # ---кол-во запусков процессов и задач
    # --- Номер таска в одном процессе все время будет увеличиваться
    if process in dG:
        dG[process] = dG[process] + 1
    else:
        dG[process] = 1


    asyncio.run(main(prm)) #Запуск процедур asyncio


    end = datetime.datetime.now()
    s = start.strftime('%H:%M:%S')
    e = end.strftime('%H:%M:%S')
    dur = (end - start)
    out = f'{process} ---cnt= s:{s} e: {e} dur:{end - start}'
    print(out)





if __name__ == '__main__':

    with open('pool_async.txt','w'):
        pass

    print('---start--')

    poolSize = 2
    task_range=20
    chunck_size=3


    #l_rn = range(0,5)
    #l_rn = [chr(x) for x in range(65,95)]
    l_rn = [str(x) for x in range(1,task_range)]
    l_chs = chunk_list(l_rn,chunck_size)   #Разбивка списка задач на список списков
    start_tm = datetime.datetime.now()

    manager = Manager()
    d = manager.dict()
    #lock = manager.Lock()  При использовании lock на запись будет зависание.
    #Без использования не все записи записываются в файл логов

    global dG
    dG = d

    for x in l_chs:
        pool_task(x)

    #asyncio.run(main(l_rn))

    end_tm = datetime.datetime.now()

    print('total:',end_tm-start_tm)

    #test_connect('a')

    print('---end---')

    print(d)