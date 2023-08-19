import urllib.request
import random
import json

import pandas as pd
import datetime

username = 'LrY7Iy603eXen5cO'
password = 'wifi;th;;satun;'
country = 'TH'
#entry = ('LrY7Iy603eXen5cO:wifi;ch;;aargau;@proxy.froxy.com:9000' ) #true
entry = ('LrY7Iy603eXen5cO:wifi;th;;satun;@proxy.froxy.com:9002')
#entry = ('LrY7Iy603eXen5cO:wifi;co;;departamento+de+tolima;@proxy.froxy.com:9007')
query = urllib.request.ProxyHandler({
    'http': entry,
    'https': entry,
})
#execute = urllib.request.build_opener(query)


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
    finally:
        #print(res)
        with open(file,'a',encoding="utf-8") as f:
            line = f'{err}#,#{country}#,#{connection}#,#{res}\n'
            f.write(line)



if __name__ == '__main__':

    start = datetime.datetime.now()

    file = 'check_result_a.csv'

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



    for i,r in p_err.iterrows():
        check_connect(r)


    end = datetime.datetime.now()

    print(end-start)