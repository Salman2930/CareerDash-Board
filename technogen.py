import requests
import re
import pandas as pd

url = 'https://api.ceipal.com/bVlWVHd0MUo4L01uMzlvaTNrSG1RZz09/job-postings/?page=1'
r = requests.get(url)
soup_data = r.json()
final_data = []
for job in soup_data['results']:
    content = {}
    content['Company Name'] = 'Technogen'
    content['Title'] = job['position_title']
    content['Job Code'] = job['job_code']
    content['Location'] = job['city']
    content['Apply Link 1'] = job['apply_job']
    content['Apply Link 2'] = job['apply_job_without_registration']
    final_data.append(content)
technogen_data_df = pd.DataFrame(final_data)
technogen_data_df
#technogen_data_df.to_excel('technogen.xlsx', index = False)

