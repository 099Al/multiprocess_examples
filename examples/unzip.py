import os
from zipfile import ZipFile
import datetime
import time
from multiprocessing import Pool, Manager, cpu_count, current_process
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import as_completed
import json
from functools import partial

cpu_n = cpu_count()

path_to_zip_folder = r'D:\Temp\SRC'
#zip_file = "ClinicalTrialArch"
zip_file = "arch2"
#path_to_unzip_folder = "/dbfs/mnt/raw/ClinicalTrials.gov/Batches/"

#Путь к скаченному архиву
path_zip = os.path.join(path_to_zip_folder,zip_file)

path_unzip = r'D:\Temp\TRG'

folder_dt = '20230112'

def f_uploaded(path_unzip_folder):
    l_uploaded = []
    for root, dirs, files in os.walk(path_unzip_folder):
        path_unzip_folder = (path_unzip_folder + "/").replace('//', "/")
        for f in files:
            file_path = os.path.join(root, f)
            size = os.path.getsize(file_path)

            if (size > 0):
                dir_file = os.path.join(root.replace(path_unzip_folder, ''), f)
                l_uploaded.append(dir_file)
    return set(l_uploaded)



#----------------------------
def f_zero(file):
    if os.path.getsize(file)==0:
        return 1
    else:
        return 0

def f_uploaded_p(path_unzip_folder):
    l_uploaded = []
    args = [(root, dirs, files) for root, dirs, files in os.walk(path_unzip_folder)]

    with Pool(50) as pool:
        pass
    '''Добавить очередь в очередь добавлять файл, если он не пустой'''
    return set(l_uploaded)
#--------------------------------------

def unzip_files(files_range, path_to_zip, path_to_unzip, files_list):
    #global listenerQ  #вынесена в global в initQueue
    a, b = files_range
    filenames = files_list[a:b]


    process = current_process()
    worker_name = process.name
    # get the name for the current worker process
    p_name = process.name

    print(p_name,a,b,'cnt:',len(filenames))

    with ZipFile(path_to_zip, 'r') as handle:

        filenames = filenames[1:]

        for filename in filenames:
            time.sleep(0.5)
            handle.extract(filename, path_to_unzip)
            #_______!!!!!!!!-----TEST-------------
            '''
            file_path = os.path.join(path_to_unzip,filename)
            file_path = file_path.replace('/', '\\')

            folder = os.path.dirname(file_path)
            chek_dir = os.path.exists(folder)
            if chek_dir==False:
                os.mkdir(folder)

            with open(file_path,'w') as file:
                file.write('1')
            '''
            #--------------------------------

            arg = (f'work:{p_name} {filename}, range:{a}-{b}, [{filenames[0]}...{filenames[-1]}]',)
            listenerQ.put(arg)


            #print('unzip',arg,worker_name)

    print(f"{a,b} from {filenames[0]} to {filenames[-1]} finished", datetime.datetime.now().strftime('%H:%M:%S'))

    return filenames

def initQueue(q):
    global listenerQ
    listenerQ = q


def unzipStatus(q, files_cnt):
    step = 5
    s = 0
    all_tasks = files_cnt
    print('status:')

    log_file = path_to_zip_folder + 'log_unzip_' + folder_dt.replace('/', '_') + '.log'
    with open(log_file, 'w') as file:
        pass

    while True:
        #time.sleep(1)
        #res = q.get()
        prev_qs=0
        qs = q.qsize()
        res=''


        #time.sleep(1)

        if qs > prev_qs:
            tasks_remain = all_tasks - qs
            msg = f"remain {tasks_remain} files. s={s},qsize={qs} time={datetime.datetime.now().strftime('%H:%M:%S')}\n"
            print(msg)

            with open(log_file, 'a') as file:
                #file.write(f"qsize={qs}, time={datetime.datetime.now().strftime('%H:%M:%S')}\n")
                file.write(msg)

            prev_qs=qs
            s = 0

        if res == 'stop':
            print('finished')
            break


def unzip_mp_chunk(path_to_zip, path_unzip_folder, workers):
    # start = datetime.datetime.now()
    set_uploaded = f_uploaded(path_unzip_folder)
    with ZipFile(path_to_zip, 'r') as handle:
        s_all_files = set(handle.namelist())
        s_uploaded = f_uploaded(path_unzip)
        files = sorted(list(s_all_files - s_uploaded ))

        print("all files in archive:", len(s_all_files ))
        print("to load:", len(files))
        print("previous loaded:", len(s_uploaded))
        print('uploaded:',(s_uploaded))

        if len(files) == 0:
            return

    n_workers = workers
    chunksize = round(len(files) / n_workers)
    # start the thread pool
    print('workers:', n_workers, 'chuncksize:', chunksize)

    l_file_ranges = []
    for x in range(0, len(files), chunksize):
        p = (x, x + chunksize)
        l_file_ranges.append(p)





    manager = Manager()
    q = manager.Queue()

    with Pool(n_workers, initializer=initQueue, initargs=(q,)) as pool:

        task_unzip = partial(unzip_files
                             , path_to_zip=path_to_zip
                             , path_to_unzip=path_unzip_folder
                             , files_list=files
                             )

        pool.apply_async(unzipStatus, (q, len(files)))
        # _ = pool.map(unzip_files2, l_file_ranges)

        #print('l_file_ranges',l_file_ranges)

        res = pool.map(task_unzip, l_file_ranges)

        for r in res:
            print('res',r,len(r))

        # Ожидаем завершения работы map, чтобы перейти к след. шагу
        q.put('stop')  # для завершения async процесса
        pool.close()

if __name__ == '__main__':

    start = datetime.datetime.now()
    unzip_mp_chunk(path_to_zip=path_zip
             ,path_unzip_folder=path_unzip
             ,workers=cpu_n)
    end = datetime.datetime.now()
    print(f"unzip duration:{end-start}")
