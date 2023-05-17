import requests
from bs4 import BeautifulSoup
import re
import pandas as pd


def get_zoho():
    url = 'https://careers.zohocorp.com/recruit/v2/public/Job_Openings?pagename=Careers&source=CareerSite&extra_fields=%5B%22Remote_Job%22%5D'
    r = requests.get(url)
    # soup = BeautifulSoup(r.content, 'html5lib')
    # print(soup)
    job_datas = r.json()['data']
    zoho_datas = []
    for data in job_datas:
    
        content={}
        content['Company Name'] = 'Zoho'
        content['Job Title'] = data['Job_Opening_Name']
        content['Job Type'] = data['Job_Type']
        content['Location'] = data['City']
        content['Apply Link'] = data['$url']
        zoho_datas.append(content)
    zoho_job_data_df = pd.DataFrame(zoho_datas)
    # zoho_job_data_df.to_excel('Zoho job list.xlsx', index = False)
    return zoho_job_data_df