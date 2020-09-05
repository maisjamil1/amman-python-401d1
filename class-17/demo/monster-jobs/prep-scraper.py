import requests
from bs4 import BeautifulSoup

URL = "https://www.monster.com/jobs/search/?q=python&where=Seattle__2C-WA"

# send a request
response = requests.get(URL)
# print(dir(response))

# get data from response
# print(response.content)

# process the data

# extract text from data using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')
results = soup.find(id="SearchResults")
# print(results.prettify())

jobs_list = results.find_all('section', class_="card-content")
# print(len(jobs_list))
# print(jobs_list[8])

formatted_jobs_list = []
for job in jobs_list:
    if job.find('div', class_='location'):
        location = job.find('div', class_='location').text.strip()
    if job.find('div', class_='company'):
        company = job.find('div', class_='company').text.strip()
    if job.find('h2', class_='title'):
        title = job.find('h2', class_='title').text.strip()
    formatted_job = { 'title': title,
                    'company': company,
                    'location': location }
    print(formatted_job)
    formatted_jobs_list.append(formatted_job)


# print(formatted_jobs_list)
# print(formatted_jobs_list[-1]['title'])
# print('*'*20)
# print(formatted_jobs_list[-1]['company'])
# print('*'*20)
# print(formatted_jobs_list[-1]['location'])

# show data to user or save it to DB
