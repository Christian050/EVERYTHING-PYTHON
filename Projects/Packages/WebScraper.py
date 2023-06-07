import requests
from bs4 import BeautifulSoup
    
def Scrape(url):
    response = requests.get(url)

    # Parsing
    soup  = BeautifulSoup(response.text, 'html.parser')


    # Extracting data
    title = soup.find('h1').text
    paragraphs = soup.find_all('p')
    for p in paragraphs:
        print(p.text)
    