from multiprocessing import Process, Value, Lock, Manager

from random import randint
import time


#Список задач для обработки
tasks = (x for x in range(0,10))


#Какая-то обработка, выполняющаяся в параллели
def task_execute(p, q, v):
    rv = randint(0,p)
    q.put((p,rv))
    #print('t',p)
    v.value += 1

    return (p,rv)

def listener(queue,v):

    cnt = 0
    while True:

        cnt = cnt+1
        #С задержкой показания статуса будут сильно отставать
        #Для вывода актуального значения в listener не должно быть задержки,
        #Тогда из очереди будет браться результат сразу как в нее попадет элемент
        #time.sleep(1)

        q = queue.get()
        qs = queue.qsize()

        #Если в очереди нет элементов
        #то queue.get() ничего не вернет. Будет в процессе ожидания нового элемента
        if q == 'stop':
            break

        print(f'status q_size={qs} el={q} cnt={cnt} value={v.value}')




if __name__ == '__main__':

    manager = Manager()
    queue = manager.Queue()  # Очередь передается в статус-Process и в Process-обработки
    value = Value('i',0)

    processes = [Process(target=task_execute, args=(i,queue,value)) for i in tasks]

    #Просмотр статуса
    status = Process(target=listener,args=(queue,value))
    status.start()

    for p in processes:
        p.start()
        p.join()

    print('---end---------')
    queue.put('stop') # Флаг остановки очереди

    status.join() #Иначе будет ошибка, т.к. основной поток завершится

    #print(queue.qsize())

