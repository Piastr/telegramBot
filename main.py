import requests
from bs4 import BeautifulSoup
import random
list_compliments = []

url = 'https://t-loves.narod.ru/komplimenty-devushke.htm'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
items = soup.find_all('p')




for i in range(len(items) - 1):
    list_compliments.append(items[i].text)
    list_compliments[i] = list_compliments[i].replace('\n', '')
    list_compliments[i] = list_compliments[i].replace('\t', '')



#https://horo.mail.ru/prediction/sagittarius/today/
#https://horo.mail.ru/prediction/aquarius/today/

def goroscope(url):
    list_aqua = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', class_='article__item article__item_alignment_left article__item_html')
    p_quotes = soup.find_all('p')
    for i in range(len(p_quotes)):
        list_aqua.append(p_quotes[i].text)
    text_return = list_aqua[0] + list_aqua[1]
    return text_return


# 2 - Первые блюда, 3 - вторые блюда, 35 - салаты, 926 - завтраки
def get_recipe(type):
    list_recipe = []
    link = 0
    x = random.randint(0, 520)
    y = x // 52
    z = x % 52
    url = f"https://www.russianfood.com/recipes/bytype/?fid={type}&page={y}#rcp_list"
    responce = requests.get(url)
    soup = BeautifulSoup(responce.text, 'lxml')
    text_first_course = soup.find_all('div', class_='recipe_l in_seen v2')
    for k in range(len(text_first_course)):
        if k == z:
            recipe_name = text_first_course[k].find('div', class_='title')
            list_recipe.append(recipe_name.text.strip())
            for a in text_first_course[k].find_all('a'):
                link = a.get('href')
            list_recipe.append(link)
    return list_recipe



#❤
