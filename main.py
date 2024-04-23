import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'http://quotes.toscrape.com/'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.content, 'lxml')
    
    # Find all the quote blocks on the page
    quote_blocks = soup.find_all('div', class_='quote')
    
    # Extract quotes and authors from each block
    for quote_block in quote_blocks:
        quote = quote_block.find('span', class_='text').text.strip()
        author = quote_block.find('small', class_='author').text.strip()
        print(f'Quote: {quote}\nAuthor: {author}\n')
else:
    print('Failed to retrieve the web page.')