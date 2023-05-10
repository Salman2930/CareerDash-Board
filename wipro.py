import requests
import re
import pandas as pd
import json

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' 
           '(KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
#def get_wipro():
url = 'https://careers.wipro.com/api/jobs?page={}&country=India&sortBy=relevance&descending=false&internal=false&deviceId=2327555526&domain=wipro.jibeapply.com'
page_no = 0
final_data = []
while True:
    r = requests.get(url.format(page_no),headers = headers)
    datas = json.loads(r.content)
    for data_list in datas['jobs']:
        content ={}
        content['Job Title'] = data_list['data']['title']
        content['Job ID'] = data_list['data']['slug']
        content['Experiance'] = data_list['data']['tags4']
        content['Apply link'] = data_list['data']['apply_url']
        content['Location'] = data_list['data']['city']
        final_data.append(content)
    page_no += 1
    if page_no > 99:
        break

    
jobs_list_jobs_Data = pd.DataFrame(final_data)
jobs_list_jobs_Data

    #jobs_list_jobs_Data.to_excel('wipro jobs.xlsx' , index = False)


