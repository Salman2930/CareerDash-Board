import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' 
           '(KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}

def get_deloit():
    url = 'https://usijobs.deloitte.com/careersUSI/SearchJobsAJAX?s=1/&jobOffset={}'
    pg_num = 0
    deloit_list = []
    while True:
        
        r = requests.get(url.format(pg_num), headers = headers)
        soup = BeautifulSoup(r.content, 'html5lib')

        for article in soup.find_all('div', {'class':'article__content--result'}):
            name = article.find('h3').text
            link = article.find('a')['href']
            location = article.find('div' , {'class' : 'article__header__text__subtitle'}).find_all('span')[-1].text

            deloit_list.append([name.strip(), link , location])
            
        pg_num += 10
        
        if pg_num > 80:
            break
            
    deloit_list_df = pd.DataFrame(deloit_list, columns = ['Job Title', 'URL', 'Location'])
      
    #deloit_list_df.to_excel('Deloit.xlsx', index = False)
    return deloit_list_df