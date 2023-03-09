from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://codefinity-content-media.s3.eu-west-1.amazonaws.com/18a4e428-1a0f-44c2-a8ad-244cd9c7985e/page.html"
page = urlopen(url)
html = page.read().decode('utf-8')

soup = BeautifulSoup(html, 'html.parser')
for img in soup.find_all('img'):
    print(img.attrs.get('src'))

for div in soup.find_all('div', {'class': 'box'}):
    print(div)

print(soup.find('p', {'id': 'id2'}))

for div in soup.find_all('div'):
    print(div.attrs.get('class'))