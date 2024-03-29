def sum(num1, num2):
    result = num1 + num2
    print(result)

sum(58, 99)# calling function

def greet(name):
    print(f'Hello {name}!')

greet('Mercy')

#Write a function that checks for even number between 1 and 20

def even_numbers():
    for values in range(1, 20):
        if (values % 2 == 0):
            print(values)

even_numbers()

#Parameters
def even_numbers(limit):
    for values in range(1, limit):
        if (values % 2 == 0):
            print(values)

even_numbers(100)
greet('Joy')

#Write a function that takes in the name and score of a student as the parameter and prints them out in a statement
def name_score(name, score):
    print(f'Hey am {name} and I scored {score}  percent in science')

name_score('John Mark', 45)

#ASSIGNMENT 
#You are given a list of dictionaries representing products and their prices. Your task is to write a Python function to find and return the product with the highest price.
  
products = [
    {'name': 'laptop', 'price': 1200},
    {'name': 'Smartphone', 'price': 800},
    {'name': 'Tablet', 'price': 500},
    {'name': 'Headphones', 'price': 120}
]


#Finding product with the highest value
def find_highest_priced_product(products):
    highest_price = float('-inf')
    highest_product_name = None

    for product in products:
        price = product['price']
        if price > highest_price:
            highest_price = price
            highest_product_name =product['name']

    print(f'Product with the highest price is a {highest_product_name} which has a price of {highest_price} ')

       
find_highest_priced_product(products)    