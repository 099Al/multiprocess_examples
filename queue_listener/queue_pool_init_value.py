from multiprocessing import Process, Value, Lock, Manager, Pool

from random import randint
import datetime
import time

from programFunctions.listener import listener

from memory_profiler import profile

#Список задач для обработки
tasks = (x for x in range(0,20))


#Какая-то обработка, выполняющаяся в параллели

def task_execute(p):
    #time.sleep(3) Чтобы статус отрабатывал корректно, т.е. чтобы очередь не накапливалась
    v = randint(0,p)

    print('t', p)
    time.sleep(0.5)
    with lG:
        vG.value += 1


    return (p,v)



def initPool(q,v,l):
    global qG, vG, lG
    qG = q
    vG = v
    lG = l


if __name__ == '__main__':

    manager = Manager()
    queue = manager.Queue()  # Очередь передается в статус-Process и в Process-обработки
    value = manager.Value('i',0)
    lock = manager.Lock()
    # Просмотр статуса
    # Статус будет запаздывать в этом примере
    # Очередь накапливается
    #status = Process(target=listener2, args=(value,))
    #status.start()

    #apply останавливает основной поток,
    #поэтому статус должен запускаться раньше
    with Pool(5, initializer= initPool, initargs=(queue,value,lock)) as pool:
        pool.apply_async(listener, args=(value,))   #Поток проверки статуса запускается здесь, иначе цикл не завершится
        processes = pool.map(task_execute,tasks)



    print('---end---------')
    queue.put('stop') # Флаг остановки очереди.  Без данного флага будет ошибка BrokenPipeError
    #Очередь отработает полностью

    #status.join() #В данном случае без join поток корректно завершается Win10. На Win11 не завершается корректно

    #print(queue.qsize())

