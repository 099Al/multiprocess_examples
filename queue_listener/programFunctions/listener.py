import time
import datetime

def listener(v):

    while True:

        time.sleep(0.1)
        v_i = v.value
        dt = datetime.datetime.now().strftime('%H:%M:%S')
        print(f'status value={v_i} time={dt}')
