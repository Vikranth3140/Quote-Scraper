import requests
from bs4 import BeautifulSoup

# Base URL of the website to scrape
base_url = 'http://quotes.toscrape.com'
# Initial page URL
url = base_url + '/page/1'

# Function to scrape quotes and authors from a page
def scrape_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'lxml')
        quote_blocks = soup.find_all('div', class_='quote')
        for quote_block in quote_blocks:
            quote = quote_block.find('span', class_='text').text.strip()
            author = quote_block.find('small', class_='author').text.strip()
            print(f'Quote: {quote}\nAuthor: {author}\n')

# Scraping the first page
scrape_page(url)

# Scraping subsequent pages if available
page_num = 2
while True:
    next_page = base_url + f'/page/{page_num}'
    response = requests.get(next_page)
    if response.status_code == 200:
        print(f'Scraping page {page_num}...')
        scrape_page(next_page)
        page_num += 1
    else:
        break