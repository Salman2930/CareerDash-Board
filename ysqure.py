import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


def get_ysqure():

    url = 'https://ysquaretechnology.com/careers/'

    url_data = requests.get(url)

    soup_data = BeautifulSoup(url_data.content, 'html5lib') 

    

    jobs = soup_data.find('div' , class_ = 'career_faq_area').find_all('div' , class_ = 'faq_area')

    data_list = []

    for job in jobs:
        job_title = job.find('div' , class_ = 'd-flex justify-content-between').find_all('p')[0].text
        job_exp = job.find('div' , class_ = 'd-flex justify-content-between').find_all('p')[1].text
        job_link = job.find('span' , class_ = 'show-lg').find('a')['href']
        job_skill = job.find('div' , class_ = 'col-lg-5').find_all('p')[-1].text
        
        content = {}
        content['Job Title'] = job_title
        content['Experiance'] = job_exp
        content['Skills'] = job_skill
        content['Apply link'] = job_link
        
        data_list.append(content)
    ysqure_jobs_df = pd.DataFrame(data_list)
    return ysqure_jobs_df
        
    
    