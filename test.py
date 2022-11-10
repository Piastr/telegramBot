import requests
from bs4 import BeautifulSoup




def get_sinonims(word):
    list_sinonims = []
    url = f'https://kartaslov.ru/синонимы-к-слову/{word}'
    responce = requests.get(url)
    soup = BeautifulSoup(responce.text, 'lxml')
    sinonims = soup.find_all('ul', class_='v2-syn-list')
    dop_sinonims = soup.find_all('ul', class_='v2-syn-list v2-syn-head-list')
    for i in sinonims:
        x = i.find_all('li')
        for k in x:
            y = k.find('a').text
            if y not in list_sinonims:
                list_sinonims.append(y)
    return list_sinonims
for i in get_sinonims('12312'):
    print(i)