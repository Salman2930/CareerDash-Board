import requests
import pandas as pd
import re
from bs4 import BeautifulSoup as sk

url = 'https://www.globallogic.com/career-search-page/page/{}/?keywords&experience&freelance&locations=india&remote'
final_data = []
pg_no = 0
while True:

    r = requests.get(url.format(pg_no))

    soup = sk(r.content, 'html5lib')
    soup_data = soup.find('div' , {'class' : 'spinner-controls'}).find_all('div' , {'class' : 'career-pagelink'})

    for cat in soup_data:

        title = cat.find('p' , {'class' : 'mb-0'}).find('a').text
        exp = cat.find('p' , {'class' : 'id-num'}).text
        link =  cat.find('p' , {'class' : 'mb-0'}).find('a')['href']
        content = {}
        content['Company Name'] = 'Globallogic'
        content['Job Title'] = title
        content['Expericane & Location'] = exp
        content['Apply Here'] = link
        final_data.append(content)

    pg_no += 1
    if pg_no > 7:
        break
globic_df_data = pd.DataFrame(final_data)
globic_df_data
