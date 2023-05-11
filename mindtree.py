import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' 
           '(KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}

def get_mindtree():
    url = 'https://careers.ltimindtree.com/search/?q=&sortColumn=referencedate&sortDirection=desc&startrow={}'
    final = []
    pag_no = 0
    while True:
        r = requests.get(url.format(pag_no) , headers = headers)
        soup_data = BeautifulSoup(r.content , 'html5lib')
        # print(soup_data)
        jobs_data = soup_data.find('tbody').find_all('td' , {'class' : 'colTitle'})

        for job in jobs_data:

            job_title = job.find('span' , {'class' : 'jobTitle hidden-phone'}).find_all('a')[-1].text
            job_link = 'https://careers.ltimindtree.com' + job.find('span' , {'class' : 'jobTitle hidden-phone'}).find_all('a')[0]['href']
            job_location = job.find('span' , {'class' : 'jobLocation visible-phone'}).find('span' , {'class' : 'jobLocation'}).text
            job_org = 'MindTree'

            content = {}
            content['Company Name'] = job_org
            content['Job Title'] = job_title
            content['Job Location'] = job_location
            content['Apply Link'] = job_link

            final.append(content)
        pag_no += 25
        if pag_no > 400:
            break
    jobs_list_jobs_Data = pd.DataFrame(final)
    return jobs_list_jobs_Data
    #jobs_list_jobs_Data.to_excel('MindTree Jobs.xlsx', index = False)