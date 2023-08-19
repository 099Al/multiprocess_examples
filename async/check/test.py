import urllib.request
import random

import pandas as pd

username = 'LrY7Iy603eXen5cO'
password = 'wifi;th;;satun;'
country = 'TH'
entry = ('LrY7Iy603eXen5cO:wifi;ch;;aargau;@proxy.froxy.com:9000' )
query = urllib.request.ProxyHandler({
    'http': entry,
    'https': entry,
})
execute = urllib.request.build_opener(query)
execute.open('https://ipinfo.io',timeout=30).read()
try:
    execute.open('https://ipinfo.io').read()
except Exception as e:
    print(e)
