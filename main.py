import os
import requests
from bs4 import BeautifulSoup

# Create a directory to store scraped data if it doesn't exist
directory = 'scraped_quotes'
if not os.path.exists(directory):
    os.makedirs(directory)

# Base URL of the website to scrape
base_url = 'http://quotes.toscrape.com'
# Initial page URL
url = base_url + '/page/1'

# Function to scrape quotes and authors from a page and save to a text file
def scrape_and_save(url, page_num):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'lxml')
        quote_blocks = soup.find_all('div', class_='quote')
        filename = f'{directory}/page_{page_num}.txt'
        with open(filename, 'w') as file:
            for quote_block in quote_blocks:
                quote = quote_block.find('span', class_='text').text.strip()
                author = quote_block.find('small', class_='author').text.strip()
                file.write(f'Quote: {quote}\nAuthor: {author}\n\n')
        print(f'Quotes from page {page_num} saved to {filename}')

# Scraping the first page and saving to a text file
print(f'Scraping page 1...')
scrape_and_save(url, 1)

# Scraping subsequent pages if available and saving to text files
page_num = 2
while True:
    next_page = base_url + f'/page/{page_num}'
    response = requests.get(next_page)
    if response.status_code == 200:
        print(f'Scraping page {page_num}...')
        scrape_and_save(next_page, page_num)
        page_num += 1
    else:
        break