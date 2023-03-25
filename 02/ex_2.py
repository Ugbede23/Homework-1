import requests
from bs4 import BeautifulSoup
page_url = "https://en.wikipedia.org/wiki/Paweł_Domagała"
response = requests.get(page_url)
html_content = response.content
soup = BeautifulSoup(html_content, 'html.parser')
dob = soup.find('span', {'class': 'bday'}).text.strip()
print(dob)

import requests
from bs4 import BeautifulSoup
page_url = "https://en.wikipedia.org/wiki/Paweł_Domagała"
response = requests.get(page_url)
html_content = response.content
soup = BeautifulSoup(html_content, 'html.parser')
references = []
for item in soup.find_all('ol', {'class': 'references'}):
    for reference in item.find_all('li'):
        references.append(reference.text.strip())
print(references)

import requests
from bs4 import BeautifulSoup
page_url = "https://en.wikipedia.org/wiki/Pawe%C5%82_Domaga%C5%82a"
response = requests.get(page_url)
html_content = response.content
soup = BeautifulSoup(html_content, 'html.parser')
occupation = [li.text for li in soup.find('div', {'class': 'hlist'}).find_all('li')]
print(occupation)