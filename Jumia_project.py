import requests
from bs4 import BeautifulSoup
import re

def get_url():
    url = 'https://www.jumia.co.ke/sporting-goods/'
    response = requests.get(url)
    #print(response)

    soup = BeautifulSoup(response.content, 'html.parser')

    articles = soup.get_text('article')
    return articles

get_url()


def get_prices():
    pattern = 'KSh\s?(\d{1,3},\d{3})*'
    text = get_url()

    matches = re.findall(pattern, text)
    print(matches)

#get_prices()


'''
i) Product Name
ii) Brand Name
iii) Price (Ksh)
iv) Discount if Available (%)
v) Total Number of Reviews
vi) Product Rating (out of 5). 
'''