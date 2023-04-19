import requests , openpyxl
from bs4 import BeautifulSoup
import re
import pandas as pd

def get_capgemini():
    url = 'https://www.capgemini.com/wp-json/macs/v1/jobs?country=en-in&size=1000'
    r = requests.get(url)
    r.json()
    datas = r.json()['data']
    capgemini_job_info = []
    for data in datas:
        content = {}
        content['Company Name'] = data['brand']
        content['Job Title'] = data['title']
        content['Apply Job URL'] = data['apply_job_url']
        content['Job Type'] = data['contract_type']
        content['Department'] = data['department']
        content['Experience Level'] = data['experience_level']
        content['Location'] = data['location']
        capgemini_job_info.append(content)
        
    capgemini_job_info_df = pd.DataFrame(capgemini_job_info)
    # capgemini_job_info_df.to_excel('Capgemini job list.xlsx', index = False)
    return capgemini_job_info_df
