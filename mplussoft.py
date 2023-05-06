import requests
from bs4 import BeautifulSoup as bs
import re
import pandas as pd

url = 'https://www.mplussoft.com/career'
r = requests.get(url)
soup = bs(r.content , 'html5lib')
# print(soup)
soup_data = soup.find('section' , {'id' : 'position-open'}).find_all('div' , {'class' : 'col-12 col-md-6 col-lg-4 postCol'})
final_data = []
for job in soup_data:
    
    title = job.find('div' , {'class' : 'positionName'}).find('h3').text
    exp = job.find('div' , {'class' : 'positionName'}).find('p').text
    link1 = job.find('a')['href']
    link = 'https://www.mplussoft.com/' + link1
    content = {}
    content['Company Name'] = 'Mplussoft'
    content['Job Title'] = title
    content['Experiance'] = exp
    content['Location'] = 'Pune'
    content['Apply Link'] = link
    final_data.append(content)
mplus_data_df = pd.DataFrame(final_data)
mplus_data_df
mplus_data_df.to_excel('mplus.xlsx' , index = False)
    #print(title , exp , link )