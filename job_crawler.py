import requests 
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Austin'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'lxml')
# lxml is faster than  the inbuilt html.parser

results = soup.find(id='ResultsContainer')
#print(results.prettify())

job_elems = results.find_all('section', class_='card-content')
for job_elem in job_elems:
    # print(job_elem, end='\n'*2)
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    # This will help us get rid of the empty blocks
    if None in (title_elem, company_elem, location_elem):
        continue
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print()

python_jobs = results.find_all('h2', string=lambda text: 'python' in text.lower())
print(len(python_jobs))

for p_job in python_jobs:
    link = p_job.find('a')['href']
    print(p_job.text.strip())
    print(f"Apply here: {link}\n")