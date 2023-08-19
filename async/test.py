import threading
import queue
import time


fifo_queue = queue.Queue()

def pop_nitems(n):
    for i in range(n):
        item = fifo_queue.get()
        time.sleep(1)
        print("Thread : {}. Retrieved & Processed Item : {}".format(threading.current_thread().name, item))
        #print("Thread {}. Processed Item : {}".format(threading.current_thread().name, item))
        fifo_queue.task_done()



if __name__ == "__main__":

    for i in range(1, 13):
        fifo_queue.put("Task-{}".format(i))

    thread1 = threading.Thread(target=pop_nitems, args=(3, ), name="Process-3Items")
    thread2 = threading.Thread(target=pop_nitems, args=(4, ), name="Process-4Items")
    thread3 = threading.Thread(target=pop_nitems, args=(5, ), name="Process-5Items")

    thread1.start(), thread2.start(), thread3.start()

    fifo_queue.join()

    print("\nAll items in queue completed. Exited from Main Thread\n")
