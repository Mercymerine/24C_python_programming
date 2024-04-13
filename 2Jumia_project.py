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

'''
    with open('data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Price', 'Discount', 'Product_name', 'Ratings', 'Reviews'])
       
    '''  
       
           
            
''' 
            
            #Finding budget discount
        discounts = soup.find_all('div', class_='bdg _dsct _sm')
        def find_discount():
            for discount in discounts:
                print(discount.text)

            
                #Finding prices
        prices = soup.find_all('div', class_ = 'prc')
        def find_price():
            for price in prices:
                return(price.text)
              

                #Finding product name
        products = soup.find_all('div', class_ = 'name')
        def find_product_name():
            for product in products:
                return(product.text)
                

                #Finding ratings
        review_divs = soup.find_all('div', class_='rev' )
        def find_ratings():
                    
             #Extract information from each review<div>
             for review_div in review_divs:
                 #Extract rating
                rating_div =review_div.find('div', class_='stars _s')
                    #print(rating_div)
                for ratings in rating_div:
                    return(ratings.text)
                   
                
        # Finding reviews
        reviews = soup.find_all('div', class_ ='rev')
        def find_reviews():
            #Extracting reviews
            for review in reviews:
                return(review.text)
               

                
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

                

                
      

        for price, discount, product_name, rating, review in (prices, discounts, product_name, ratings, reviews):
            writer.writerow ([price, discount, product_name, rating, review])
        
        with open('data.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['price'])
                for price in prices:
                    writer.writerow([price.text])
        
    

get_url('https://www.jumia.co.ke/hair-care-d/')


'''