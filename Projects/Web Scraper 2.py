import requests
from bs4 import BeautifulSoup

# Http request
url = 'https://www.sportskeeda.com/esports/best-cod-mobile-sensitivity-settings-2022-recoil'
response = requests.get(url)

# Parse
soup = BeautifulSoup(response.content, 'html')
print(soup)