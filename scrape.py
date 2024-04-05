# requests library --> sends https requests to a website and get a response
# beautifulsoup --> to pass html or xml contnent of a website and extract data

import requests
from bs4 import BeautifulSoup

url = 'https://hojaleaks.com/regular-expressions-in-python-a-comprehensive-tutorial-for-beginners'
response = requests.get(url)

#print(response.content)
soup = BeautifulSoup(response.content, 'html.parser')#lxml for xml
#print(soup)

headings = soup.find_all('h1')
#print(headings)

for heading in headings:
    print(heading.text)

paragraphs = soup.find_all('p')
#print(headings)

for paragraph in paragraphs:
    print(paragraph.text)