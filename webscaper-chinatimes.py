import requests
import time, random
from fake_useragent import UserAgent
import pandas as pd
from bs4 import BeautifulSoup as bs

ua = UserAgent()
headers = {
    'User-Agent': ua.random
}

url_chinatimes = "https://www.chinatimes.com/?chdtv"
res_chinatimes = requests.get(url=url_chinatimes, headers=headers)
soup_chinatimes = bs(res_chinatimes.text,'lxml')
focus_news = soup_chinatimes.select('li.col-md-6')

title = [i.select('h3.title')[0].text for i in focus_news]
urls = [i.select('h3.title')[0].a['href'] for i in focus_news]
category = [i.select('div.category')[0].text for i in focus_news]
time = [i.select('time')[0].text for i in focus_news]

zipped = zip(title,urls,category,time)
df_chinatimes = pd.DataFrame(list(zipped), columns=['title', 'url','tags','time'])
print(df_chinatimes)