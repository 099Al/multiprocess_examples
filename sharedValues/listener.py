from multiprocessing import Process, Value, Lock, Manager

from random import randint

tasks = (x for x in range(0,20))


def task_execute(p, q):
    v = randint(0,p)
    q.put((p,v))
    print('t',p)
    return (p,v)

def listener(q):

    pass


if __name__ == '__main__':

    manager = Manager()
    queue = manager.Queue()

    processes = [Process(target=task_execute, args=(i,queue)) for i in tasks]


    for p in processes:
        p.start()
        p.join()

    print('---end---------')

    print(queue.qsize())

    for q in range(queue.qsize()):
        x = queue.get()
        print('q',x)