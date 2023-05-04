import requests
from bs4 import BeautifulSoup as sk
import pandas as pd
import re

url  = 'https://www.testingxperts.com/company/career/?utm_source=GBP-Chd'
r = requests.get(url)
soup = sk(r.content, 'html5lib')
#print(soup)
job = soup.find('div', {'class' : 'career-open-list'}).find('tbody').find_all('tr')

final_data = []

for jobs in job:
    title = jobs.find_all('td')[0].text
    dep = jobs.find_all('td')[2].text
    exp = jobs.find_all('td')[1].text
    location = jobs.find_all('td')[3].text
    link = jobs.find('td').find('a')['href']
    content = {}
    content['Title'] = title
    content['Department'] = dep
    content['Experiance'] = exp
    content['Location'] = location
    content['Apply'] = link
    
    final_data.append(content)
    
test_data_df = pd.DataFrame(final_data)
test_data_df
test_data_df.to_excel('jobs.xlsx' , index = False)
