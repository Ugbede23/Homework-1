import requests
from bs4 import BeautifulSoup
page_url = "https://www.pythonscraping.com/pages/page3.html"
response = requests.get(page_url)
html_content = response.content
bs = BeautifulSoup(html_content,'html.parser')
footer = bs.find('div', {'id':'footer'})
footer_text = footer.get_text()
print(footer_text)

import requests
from bs4 import BeautifulSoup
page_url = "https://www.pythonscraping.com/pages/page3.html"
response = requests.get(page_url)
html_content = response.content
soup = BeautifulSoup(html_content, 'html.parser')
Bold = soup.find_all('span', {'class': 'excitingNote'})
bolded = [note.text.strip() for note in Bold]
print(bolded)

import requests
from bs4 import BeautifulSoup
page_url = "https://www.pythonscraping.com/pages/page3.html"
response = requests.get(page_url)
html_content = response.content
soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find('table', {'id': 'giftList'})
last_row = table.find_all('tr')[-1]
last_item_title = last_row.find('td').text.strip()
print(last_item_title)



