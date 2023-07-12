import asyncio
import random
import time
import datetime



async def task(fix_param,param):

    print(f'start n:{param}')
    t = random.randint(1,5)
    await asyncio.sleep(t)  #если использовать time.sleep(), то будет последовательное выполнение
    task_nm = asyncio.current_task().get_name()
    print(f'end n:{param} wait:{t} fix_param:{fix_param} task_nm={task_nm}')


#Цикл, которые считывает данные из очереди и запускает task
async def scanner(const,queue):
    while True:
        param = await queue.get()

        if param is None:
            #await queue.put(param)  # Не понятно зачем это в коде
            break

        await task(const,param)
        task_nm = asyncio.current_task().get_name()

        print(f'q_size_1:{queue.qsize()} n:{param} task_nm={task_nm}')
        queue.task_done()  #исключить из очереди
        print(f'q_size_2:{queue.qsize()} n:{param}')

async def main(l_params,const_param,limit):

    queue = asyncio.Queue(10)


    #Создаются процессы-воркеры, которые читают параметры из очереди в цикле
    #asyncio.create_task - запускает функции параллельно
    _ = [asyncio.create_task(scanner(const_param,queue)) for _ in range(limit)]  #limit workers

    for p in l_params:
        await queue.put(p)

    await queue.join() #wait all task done

    await queue.put(None) # stop process



if __name__ == '__main__':
    print('---start--')


    l_params = range(0,50)

    start_tm = datetime.datetime.now()
    asyncio.run(main(l_params,'A',20))
    end_tm = datetime.datetime.now()

    print('total:',end_tm-start_tm)

    #test_connect('a')



    print('---end---')