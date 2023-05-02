import requests 
from bs4 import BeautifulSoup
import re
import pandas as pd
import json

def get_infosys():

    url = 'https://intapgateway.infosysapps.com/careersv2/search/intapjbsrch/getSearchJobs?sourceId=1,21&searchText=ALL'
    r = requests.get(url)
    r.json()
    job_datas = r.json()
    infosys_data = []

    for data in job_datas:
        content={}
        content['Company Name'] = data['company']
        content['Job ID'] = data['requisitionId']
        content['Job Title'] = data['postingTitle']
        content['Location'] = data['location']
        content['Experiance Level'] = str(data['minExperienceLevel']) +' '+ str('to')+' '+ str(data['maxExperienceLevel'])
        content['Skills'] = data['preferredSkills']
        content['Role'] = data['roleDesignation']
        infosys_data.append(content)

    infosys_job_info_df = pd.DataFrame(infosys_data)
    return infosys_job_info_df
    #infosys_job_info_df.to_excel('Infosys job list.xlsx', index = False)