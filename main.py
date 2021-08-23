from bs4 import BeautifulSoup
import requests

userLink = "https://en.wikipedia.org/wiki/Red"

def getFirstLink(link):
  page = requests.get(link)
  
  soup = BeautifulSoup(page.content, 'html.parser')
  
  index = 0
  while not soup.find(id="mw-content-text").div.findAll('p')[index].a:
    index += 1

  return "https://en.wikipedia.org" + soup.find(id="mw-content-text").div.findAll('p')[index].a['href']


while userLink != "https://en.wikipedia.org/wiki/Philosophy":
  userLink = getFirstLink(userLink)
  print(userLink)
