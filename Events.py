# https://realpython.com/beautiful-soup-web-scraper-python/

import requests
from bs4 import BeautifulSoup

URL = "https://epl.bibliocommons.com/v2/events"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")




results = soup.find(id="ResultsContainer")
job_elements = results.find_all("div", class_="card-content") # returns an interable

for job_element in job_elements:
    print(job_element, end="\n"*2)

for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text)
    print(company_element.text)
    print(location_element.text)
    print()


print(results.prettify())

for job_element in python_job_elements:
    # -- snip --
    links = job_element.find_all("a")
    for link in links:
        print(link.text.strip())




