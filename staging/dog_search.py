from bs4 import BeautifulSoup
import requests

website = requests.get("https://www.austinpetsalive.org/adopt/dogs")
soup = BeautifulSoup(website.content, 'html.parser')

frames = soup.find_all('div', {'class': 'large-tile'})

dogDict = {}
criteria = ['female', 'mix']

for frame in frames:
    dogName = (frame.find('a', {'class': 'orange'}).get_text()) #get dog name
    dogDict[dogName] = ""
    dogs = frame.find_all('li', {'class': 'burnt-orange'}) #get dog features
    for feature in dogs:
        dogDict[dogName] += feature.get_text() + " " #append features to string

for dog in dogDict:
    matches = 0 #keep track of number of matches
    for c in criteria: #goes through list of criteria
        if c in dogDict[dog].lower():
            matches += 1
    if matches == len(criteria): #checks if all criteria is met
        print(dog, dogDict[dog])
