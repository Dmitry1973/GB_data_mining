import requests

site_adr = 'https://icobench.com/icos'
N = 1

while N < 4:
    params = {'page': N}
    site = requests.get(site_adr,params=params)
    print(site.url)
    with open(f'icobench_ico_page_{N}.html', 'w', encoding='utf-8') as d:
        d.write(site.text)
    N +=1



