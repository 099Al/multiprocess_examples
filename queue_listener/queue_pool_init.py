from multiprocessing import Process, Value, Lock, Manager, Pool

from random import randint
import time


#Список задач для обработки
tasks = (x for x in range(0,120))


#Какая-то обработка, выполняющаяся в параллели
def task_execute(p):
    v = randint(0,p)
    qG.put((p,v))
    print('t',p)
    return (p,v)

def listener(queue):

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

        print(f'status q_size={qs} el={q} cnt={cnt}')


def initPool(q):
    global qG
    qG = q


if __name__ == '__main__':

    manager = Manager()
    queue = manager.Queue()  # Очередь передается в статус-Process и в Process-обработки

    # Просмотр статуса
    # Статус будет запаздывать в этом примере
    # Очередь накапливается
    status = Process(target=listener, args=(queue,))
    status.start()

    #apply останавливает основной поток,
    #поэтому статус должен запускаться раньше
    with Pool(5, initializer= initPool, initargs=(queue,)) as pool:
        processes = pool.map(task_execute,tasks)



    print('---end---------')
    queue.put('stop') # Флаг остановки очереди.  Без данного флага будет ошибка BrokenPipeError
    #Очередь отработает полностью

    #status.join() #В данном случае без join поток корректно завершается

    #print(queue.qsize())

