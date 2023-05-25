#2
import requests
from bs4 import BeautifulSoup
response = requests.get('https://ru.wikipedia.org/')
if response.status_code == 200:
    soup = BeautifulSoup(response.text , features="html.parser")
    soup_list = soup.find_all('a')
    for link in soup_list:
        href = link.get('href')
        print(href)