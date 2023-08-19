import urllib.request
import random
import json
from concurrent.futures import  ThreadPoolExecutor, as_completed

import pandas as pd
import datetime


def check_connect(row):
    err = row['err']
    connection = row['connect']
    country = row['country']


    entry = (connection)
    query = urllib.request.ProxyHandler({
        'http': entry,
        'https': entry,
    })
    execute = urllib.request.build_opener(query)

    res = ''

    try:
        res_b = execute.open('https://ipinfo.io',
                             timeout=30).read()  # execute.open('https://ipinfo.io',timeout=30).read()
        # print(type(res_b),res_b)
        res = res_b.decode('utf8').replace('\n', '')
        # src_data = json.load(res)
        # print(res)
    except Exception as e:
        res = str(e.reason)
    except UnicodeDecodeError as e:
        res = str(res_b)
    '''
    finally:
        #print(res)
        with open('check_result_t.csv','a',encoding="utf-8") as f:
            line = f'{err}#,#{country}#,#{connection}#,#{res}\n'
            f.write(line)
    '''
    return f'{err}#,#{country}#,#{connection}#,#{res}'



if __name__ == '__main__':

    start = datetime.datetime.now()

    file = 'check_result_t.csv'

    with open(file,'w',encoding="utf-8") as f:
        f.write('err#,#country#,#connection#,#res\n')


    p_err = pd.read_csv('err_log.csv')

    print(p_err.columns)

    p_err = p_err[['date','connect','port','code']]
    p_err['err']= p_err.apply(lambda x: x['date'].split(':')[-1].upper(),axis=1)
    p_err['country'] = p_err.apply(lambda x: str(x['code']).replace('code:',''),axis=1)
    p_err['port'] = p_err.apply(lambda x: str(x['port']).replace('port:',''),axis=1)
    p_err['connect'] = p_err.apply(lambda x: str(x['connect']).replace('connect:','')+':'+x['port'].strip(),axis=1)

    p_err = p_err[['err','connect','port','country']]



    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(check_connect,row) for i,row in p_err.iterrows()]

        for fut in as_completed(futures):
            with open(file, 'a', encoding="utf-8") as f:
                f.write(fut.result()+'\n')

    end = datetime.datetime.now()

    print(end - start)