import requests ,openpyxl
from bs4 import BeautifulSoup
import pandas as pd
import re
import json

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' 
           '(KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
def get_unify():
    url = 'https://api.unifytech.com/api/v1/jobs/?country=india'

    r = requests.get(url, headers = headers)

    data_jobs = r.json()

    final_data = []

    for job_list in data_jobs:
        content = {}
        
        content['Company Name'] = 'Unify Tech'
        content['Job Title'] = job_list['title']
        content['Experiance'] = job_list['experience']
        content['No of Opening Position'] = job_list['number_of_positions']
        location_str = ''
        for loc in job_list['location']:
            loc_data = loc['city']
            location_str = location_str+' '+loc_data
            #join_data = ''.join(location_str)
            
        content['Location'] = location_str
        content['Apply Link'] = 'https://unifytech.com/company/careers/jobs/'+job_list['code']
        final_data.append(content)
        
        
        
        
            
            
            #location_str = location_str + " " + loc_data['city']
        
                
    
        
    pd_unify_data = pd.DataFrame(final_data)
    return pd_unify_data

    #pd_unify_data.to_excel('unify jobs.xlsx' , index = False)

