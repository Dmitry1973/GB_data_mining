import json
import requests
import os


my_path = 'ico/'
if not os.path.isdir(my_path):
    os.mkdir(my_path)

site_adr = 'https://icobench.com/icos'
for N in range (1, 470):
    params = {'page': N}
    site = requests.get(site_adr,params=params)
    #print(site.url)    #а потом ежик подумал, а зачем печатать ссылки:)
    with open(f'icobench_ico_page_{N}.html', 'w', encoding='utf-8') as d:
        d.write(site.text)
   



