import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

def get_spider():

    url = 'https://www.speridian.com/careers/openings/'

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')

    soup_data = soup.find('div' , {'class' : 'tg-grid-holder tg-layout-masonry'}).find_all('article' , {'class' : 'tg-item'})
    job_data = []
    for cat in soup_data:
        content = {}
        content['Company Name'] = 'speridian'
        content['Job Title'] = cat.find('div' , {'class' : 'tg-item-content-holder tg-dark standard-format'}).find('h2' , {'class' : 'tg-item-title'}).find('a').text
        content['Job Link'] = cat.find('div' , {'class' : 'tg-item-content-holder tg-dark standard-format'}).find('h2' , {'class' : 'tg-item-title'}).find('a')['href']
        job_data.append(content)
    spider_df_data = pd.DataFrame(job_data)
    return spider_df_data
    #spider_df_data.to_excel('Spider.xlsx', index = False)