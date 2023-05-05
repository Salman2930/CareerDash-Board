import requests
from bs4 import BeautifulSoup as SK
import pandas as pd
import re
import json

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' 
           '(KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}

url = 'https://careers.anthology.com/search/jobs/in?location=india&page={}&q=#'
pg_no = 0
final_data = []

while True:
    #print(pg_no)
    r = requests.get(url.format(pg_no), headers = headers)
    soup = SK(r.content, 'html5lib')
    #print(soup)

    soup_data = soup.find('div' , {'class':'jobs-section__list'}).find_all('div' , {'class' : 'jobs-section__item page-section-small'})
    for job in soup_data:
        title = job.find('h5').find('a').text
        location = job.find('div' , {'class':'large-4 columns'}).find('span').next_sibling.replace("  ","").replace("\n","").strip()
        link = job.find('h5').find('a')['href']
        content = {}
        content['Company Name'] = 'Anthology'
        content['Job Title'] = title
        content['Location'] = location
        content['Apply Link & JD'] = link
        final_data.append(content)
    pg_no += 1
    
    if pg_no > 5:
        break

anthology_data_df = pd.DataFrame(final_data)
anthology_data_df
anthology_data_df.to_excel('anthology.xlsx',index = False)