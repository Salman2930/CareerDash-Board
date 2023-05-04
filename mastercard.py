import requests
import re
import pandas as pd
from bs4 import BeautifulSoup as sk
import json

url = 'https://www.epam.com/services/vacancy/search?locale=en&limit=20&recruitingUrl=%2Fcontent%2Fepam%2Fen%2Fcareers%2Fjob-listings%2Fjob&query=&country=India&sort=relevance&offset=40&searchType=placeOfWorkFilter&_=1675779201706'
r = requests.get(url)
job = r.json()
print(job)
final_data = []
for cat in job['result']:
    content = {}
    content['Company Name'] = 'EPAM'
    content['Job Title'] = cat['name']
    content['Location'] = cat['localizedCity']
    content['Apply Here'] = cat['url']
    final_data.append(content)
epam_df_data = pd.DataFrame(final_data)
epam_df_data
epam_df_data.to_excel('epam jobs.xlsx' , index = False)