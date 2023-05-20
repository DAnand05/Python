import requests
from bs4 import BeautifulSoup
import tkinter as tk

# Create a function to search for and compare prices of a product
def search_and_compare(product_name):
    # Define the URL of the product on different ecommerce websites
    flipkart_url = "https://www.flipkart.com/search?q=" + product_name
    amazon_url = "https://www.amazon.in/s?k=" + product_name

    # Send requests to the URLs and get the HTML response
    flipkart_response = requests.get(flipkart_url).content
    amazon_response = requests.get(amazon_url).content

    # Parse the HTML response using BeautifulSoup
    flipkart_soup = BeautifulSoup(flipkart_response, 'html.parser')
    amazon_soup = BeautifulSoup(amazon_response, 'html.parser')

    # Find the prices of the product on Flipkart and Amazon
    flipkart_price_element = flipkart_soup.find('div', {'class': '_1vC4OE _2rQ-NK'}).text

    if flipkart_price_element is not None:
        flipkart_price = flipkart_price_element.text
        print(flipkart_price)
    else:
        print('Price not found on Flipkart')

    amazon_price = amazon_soup.find('span', {'class': 'a-price-whole'}).text

    # Display the prices in a GUI window
    window = tk.Tk()
    window.geometry('300x200')
    window.title('Product Prices')

    tk.Label(window, text='Flipkart Price: ' + flipkart_price).pack(pady=5)
    tk.Label(window, text='Amazon Price: ' + amazon_price).pack(pady=5)

    window.mainloop()

# Accept the product name from the user
product_name = input('Enter the product name: ')

# Call the search_and_compare function with the product name
search_and_compare(product_name)
