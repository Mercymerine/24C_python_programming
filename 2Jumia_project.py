import requests
from bs4 import BeautifulSoup
import re
import csv

def get_url(url):
    response = requests.get(url)
    #print(response.content)

    soup = BeautifulSoup(response.content, 'html.parser')
    #print(soup)

    with open('data.csv', 'w', newline='') as csvfile:
            #Finding budget discount
        discounts = soup.find_all('div', class_='bdg _dsct _sm')
        def find_discount():
            for discount in discounts:
                if discount:
                    print(discount.text)
                else:
                    print('Not found')
            
                #Finding prices
        prices = soup.find_all('div', class_ = 'prc')
        def find_price():
            for price in prices:
                if price:
                    return(price.text)
                else:
                    return('Not found')

                #Finding product name
        products = soup.find_all('div', class_ = 'name')
        def find_product_name():
            for product in products:
                if product:
                    return(product.text)
                else:
                    return('Not found')

                #Finding ratings
        review_divs = soup.find_all('div', class_='rev' )
        def find_ratings():
                    
             #Extract information from each review<div>
             for review_div in review_divs:
                 #Extract rating
                rating_div =review_div.find('div', class_='stars _s')
                    #print(rating_div)
                for ratings in rating_div:
                    if ratings:
                        return(ratings.text)
                    else:
                         return('Rating not found')
                
        # Finding reviews
        reviews = soup.find_all('div', class_ ='rev')
        def find_reviews():
            #Extracting reviews
            for review in reviews:
                if review:
                    return(review.text)
                else:
                    return('Review not found')

                '''
                #Finding the brand name
                a_tag = soup.find_all('a', class_='_more')
                #print(a_tag)

                if a_tag:
                    brand_name = a_tag.get_text(strip=True)
                    brand_url = a_tag['href']

                    print("Brand Name:", brand_name)
                    print("Brand URL:", brand_url)
                else:
                    print("Brand not found.")

                '''

                
        writer = csv.writer(csvfile)
        writer.writerow(['Price', 'Discount', 'Product_name', 'Ratings', 'Reviews'])
        for price, discount, product_name, rating, review in zip(find_price(), find_discount(), find_product_name(), find_ratings(), find_reviews()):
            writer.writerow ([price, discount, product_name, rating, review])
        '''
        with open('data.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['price'])
                for price in prices:
                    writer.writerow([price.text])
        
    '''

get_url('https://www.jumia.co.ke/hair-care-d/')


