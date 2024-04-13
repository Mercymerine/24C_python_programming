import requests
from bs4 import BeautifulSoup
import re
import csv



def get_url(url):

    
    response = requests.get('https://www.jumia.co.ke/hair-care-d/')
        #print(response.content)

    soup = BeautifulSoup(response.content, 'html.parser')
        #print(soup)

    divs = soup.find_all('div', class_ = 'itm col')
    #print(divs)

    with open('data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile) 
        writer.writerow(['Product_name', 'Prices', 'Discounts', 'Reviews and Rates'])
       

        for div in divs:
            #Finding product name
            product_name = div.find_all('div', class_='name')
            for name in product_name:
                product_name = name.text.strip()
            
            
            #Finding prices
            prices = div.find_all('div', class_ ='prc')
            for price in prices:
                prices = price.text.strip()

            #Finding discounts
            discounts = soup.find_all('div', class_='bdg _dsct _sm')
            for discount in discounts:
                discounts = discount.text.strip()

            #Finding reviews and rates
            reviews = soup.find_all('div', class_ ='rev')
            for review in reviews:
                reviews =review.text.strip()
            
            

            writer.writerow([product_name, prices, discounts, reviews])
            
            

get_url('https://www.jumia.co.ke/hair-care-d/')

