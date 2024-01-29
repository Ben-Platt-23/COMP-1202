import requests
from bs4 import BeautifulSoup

# setting the url
url = 'http://quotes.toscrape.com/'
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    html_content = response.text
else:
    print("Failed to retrieve the website")


soup = BeautifulSoup(html_content, 'html.parser')

# assigning all the rough quotes to a variable 
quote_elements = soup.findAll('div', class_='quote')

# going through the quotes
for quote in quote_elements:
    # seperating the quotes and making them look nice
    quote_text = quote.find('span', class_='text').text.strip()
    # same concept with the author names
    author_name = quote.find('small', class_='author').text.strip()
    #printing out the quote
    print(f'Quote: {quote_text}')
    #printing out the author name
    print(f'Author: {author_name}')
    #printing out three dashes to space out the quotes and their author names
    print('---')
