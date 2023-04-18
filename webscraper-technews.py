import requests
import time, random
from fake_useragent import UserAgent
import pandas as pd
from bs4 import BeautifulSoup as bs

# 科技新報
ua = UserAgent()
headers = {
    'User-Agent': ua.random
}

list_technews = []
for page in range(1,21):
    url_technews = f'https://technews.tw/category/ai/page/{page}/'
    response_technews = requests.get(url=url_technews, headers=headers)
    soup_technews = bs(response_technews.text, 'lxml')

    technews = soup_technews.find_all("div", "content")
    for i in technews:
        dict_technews={}
        dict_technews["title"] = i.find("h1", "entry-title").text
        dict_technews["url"] = i.find("h1", "entry-title").a['href']
        dict_technews["time"] = i.find_all("span", "body")[1].text
        dict_technews["tags"] = i.find_all("span", "body")[2].text.strip().replace("\t","").replace("\n", "")
        list_technews.append(dict_technews)
    time.sleep(random.uniform(2,4))
    
df_technews = pd.DataFrame(list_technews)
print(df_technews)