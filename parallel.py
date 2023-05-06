import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

def get_parallel():

    url = 'https://jobs.lever.co/parallelwireless?location=Bangalore'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')

    soup_data = soup.find('div' , {'class' : 'postings-wrapper'}).find('div' , {'class' : 'postings-group'}).find_all('div' , {'class' : 'posting'})
    final_data = []

    for cat in soup_data:
        content = {}
        
        content['Job Title'] = cat.find('a' , {'class' : 'posting-title'}).find('h5').text
        content['Job Location'] = cat.find('div' , {'class' : 'posting-categories'}).find('span').text
        content['Aplly Link'] = cat.find('a' , {'class' : 'posting-title'})['href']
        final_data.append(content)
        
    parallel_df_data = pd.DataFrame(final_data)
    return parallel_df_data