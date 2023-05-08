import requests
from bs4 import BeautifulSoup as bs
import re
import pandas as pd

def get_pubmatic():

    url = 'https://pubmatic.com/careers/job-search/?location=inPune'
    r= requests.get(url)
    soup = bs(r.content, 'html5lib')
    soup_data = soup.find('div' , {'class' : 'postings'}).find_all('a')
    final_data = []
    for cat in soup_data:
        
        content = {}
        content['Company Name'] = 'PubMatic'
        content['Job Title'] = cat.text
        content['Aplly Link'] = cat['href']
        final_data.append(content)
    pubmatic_df_data = pd.DataFrame(final_data)
    return pubmatic_df_data