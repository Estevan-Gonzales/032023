from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://codefinity-content-media.s3.eu-west-1.amazonaws.com/18a4e428-1a0f-44c2-a8ad-244cd9c7985e/jesus.html"
page = urlopen(url)
html = page.read().decode('utf-8')

soup = BeautifulSoup(html, 'html.parser')
#print(soup.prettify())

print(soup.head.prettify())

for child in soup.head.children:
    print(child)

for el in soup.ul.children:
    print(el)


print(soup.find_all('p'))

for el in soup.find_all(['div', 'title']):
    print(el)

print('\n')

print(soup.find('div'))
print(soup.find('div').attrs)
print(soup.find('div').contents)
print(soup.find('div').get_text())

print('\n')

for div in soup.find_all('div'):
    print(div.attrs)

for p in soup.find_all('p'):
    print(p.get_text())