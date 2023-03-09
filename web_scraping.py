# Importing the module
from urllib.request import urlopen

# Opening web page
url = "https://codefinity-content-media.s3.eu-west-1.amazonaws.com/18a4e428-1a0f-44c2-a8ad-244cd9c7985e/mother.html"
page = urlopen(url)
#print(page) #only returns the response (not text)

web_page = page.read().decode("utf-8") #string object
#print(type(web_page))
#print(web_page)

start = web_page.find('<title')
finish = web_page.find('</title>') + len('</title>')

print(web_page[start:finish])