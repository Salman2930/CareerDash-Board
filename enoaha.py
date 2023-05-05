import requests
import re
from bs4 import BeautifulSoup as SK
import pandas as pd


url = 'https://enoahisolution.com/job-opportunity/'

r = requests.get(url)

soup = SK(r.content, 'html5lib')
soup_data = soup.find('div' , {'class' : 'job-open-list-sec'}).find_all('div' , {'class': 'col-sm-6'})
final_data = []
for job in soup_data:
    title = job.find('a').find('div' , {'class' : 'job-title'}).text
    location = job.find('a').find('div' , {'class' : 'job-location'}).text
    exp = job.find('a').find('div' , {'class' : 'experience'}).text
    link = job.find('a')['href']
    content = {}
    content['Company Name'] = 'Enoah Isolution'
    content['Job Title'] = title
    content['Location'] = location
    content['Experiance'] = exp
    content['Apply Link & JD'] = link
    
    final_data.append(content)
enoaha_data_df = pd.DataFrame(final_data)
enoaha_data_df
enoaha_data_df.to_excel('enoaha.xlsx' , index=False)
    #print(title , location , exp , link)
    