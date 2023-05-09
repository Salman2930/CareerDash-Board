import requests
from bs4 import BeautifulSoup
import re
import json
import pandas as pd
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' 
           '(KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}

def get_ust():

    url = 'https://fa-erwh-saasfaprod1.fa.ocs.oraclecloud.com/hcmRestApi/resources/latest/recruitingCEJobRequisitions?onlyData=true&expand=requisitionList.secondaryLocations,flexFieldsFacet.values&finder=findReqs;siteNumber=CX_2,facetsList=LOCATIONS%3BWORK_LOCATIONS%3BTITLES%3BCATEGORIES%3BORGANIZATIONS%3BPOSTING_DATES%3BFLEX_FIELDS,limit=25,locationId=300000000433119,sortBy=POSTING_DATES_DESC,offset={}'
    pg_num = 0
    final_data = []
    while True:
        r= requests.get(url.format(pg_num), headers = headers)
        soup_data = r.json()
        
        for job_data in soup_data['items']:
            for cat in job_data['requisitionList']:
                content = {}
                content['Company Name'] = 'UST'
                content['Job Title'] = cat['Title']
                content['Location'] = cat['PrimaryLocation']
                content['Apply Link'] = 'https://fa-erwh-saasfaprod1.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_2/job/'+cat['Id']+'/?location=India&locationId=300000000433119&locationLevel=country&mode=location'

                final_data.append(content)
        pg_num += 25

        if pg_num > 200:
            break
    ust_data_df = pd.DataFrame(final_data)
    return ust_data_df
