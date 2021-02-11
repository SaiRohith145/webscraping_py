from bs4 import BeautifulSoup
import requests
import lxml

html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=pyhton&txtLocation=').text
soup= BeautifulSoup(html_text,'lxml')
jobs=soup.find_all('li',class_="clearfix job-bx wht-shd-bx")
for job in jobs:
    
    job_date=job.find('ul',class_="top-jd-dtl clearfix").li.text.replace('card_travel','')
    if '0' in job_date:
        c_name=job.find('h3',class_="joblist-comp-name").text.replace(' ','')
        j_skill=job.find('ul',class_="list-job-dtl clearfix").span.text.replace(' ','')
        if 'nmap' not in j_skill:
            print(f'years of exprince:{job_date}')
            print(f'company name:{c_name}')
            print(f'skills:{j_skill}')
        

