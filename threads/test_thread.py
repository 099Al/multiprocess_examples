import threading
import random
import time
import datetime






def worker(p):
    i,lock = p
    """thread worker function"""
    rand = random.randint(1,5)
    time.sleep(rand)
    #Чтобы записи в out не накладывались друг на друга
    with lock:
        print('Worker',i,rand)


if __name__=='__main__':
    threads = []
    start = datetime.datetime.now()
    lock = threading.Lock()
    for i in range(5):
        t = threading.Thread(target=worker,args=[(i,lock)])
        threads.append(t)
        t.start()
        #t.join() в этом случае код будет выполняться последовательно

    #После того как все потоки стартанули,
    # надо ставить в ожидание основного потока,
    # чтобы  следующие команды выполнялись после завершения потока
    for x in threads:
        x.join()

    duration = datetime.datetime.now() - start

    print(f"Took {duration.total_seconds():.2f} seconds.")

