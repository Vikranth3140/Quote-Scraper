import os
import logging
import requests
from bs4 import BeautifulSoup

# Create a directory to store scraped data
if not os.path.exists('scraped_quotes'):
    os.makedirs('scraped_quotes')

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Function to scrape quotes and authors from a page and save to a text file
def scrape_page(url, page_num):
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
        soup = BeautifulSoup(response.content, 'lxml')
        quote_blocks = soup.find_all('div', class_='quote')
        file_name = f'scraped_quotes/page_{page_num}.txt'
        with open(file_name, 'w', encoding='utf-8') as file:
            for quote_block in quote_blocks:
                quote = quote_block.find('span', class_='text').text.strip()
                author = quote_block.find('small', class_='author').text.strip()
                file.write(f'Quote: {quote}\nAuthor: {author}\n\n')
        logger.info(f'Page {page_num} scraped successfully.')
    except requests.RequestException as e:
        logger.error(f'Error scraping page {page_num}: {e}')

# Base URL of the website to scrape
base_url = 'http://quotes.toscrape.com'
# Initial page URL
url = base_url + '/page/1'

# Scraping the first page
scrape_page(url, 1)

# Scraping subsequent pages if available
page_num = 2
while True:
    next_page = base_url + f'/page/{page_num}'
    response = requests.get(next_page)
    if response.status_code == 200:
        logger.info(f'Scraping page {page_num}...')
        scrape_page(next_page, page_num)
        page_num += 1
    else:
        break