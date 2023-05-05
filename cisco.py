import requests
import re
from bs4 import BeautifulSoup as SK
import pandas as pd

url = 'https://jobs.cisco.com/jobs/SearchJobs/?21178=%5B207928%5D&21178_format=6020&listFilterMode=1&projectOffset={}'
pg_no = 0
final_data = []
while True:
    r = requests.get(url.format(pg_no))
    soup = SK(r.content, 'html5lib')
    # print(soup)
    soup_data = soup.find('tbody').find_all('tr')
    #final_data = []
    for job in soup_data:
        title = job.find('td', {'data-th' : 'Job Title'}).find('a').text
        location = job.find('td' , {'data-th' : 'Location'}).text
        link = job.find('td', {'data-th' : 'Job Title'}).find('a')['href']
        content = {}
        content['Company Name'] = 'Cisco'
        content['Job Title'] = title
        content['Locations'] = location
        content['Apply & JD'] = link
        final_data.append(content)
    pg_no += 25
    if pg_no >100:
        break
cisco_data_df = pd.DataFrame(final_data)
cisco_data_df
cisco_data_df.to_excel('cisco jobs.xlsx',index = False)