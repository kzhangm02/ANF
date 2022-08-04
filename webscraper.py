import requests
import datetime
from bs4 import BeautifulSoup
from xml.dom import minidom
from rfeed import *

headers = {'User-Agent': 'Chrome/103.0.0.0'}
now = datetime.datetime.now()

def elem_to_item(elem):
   title = elem.get_text()
   link = elem.get('href')
   return Item(title=title, link=link)
   
def smart_cities():
   url = 'https://www.smart-energy.com/?s=&doubleFilter=true&blockID=107975&categoryOne=9897&categoryTwo=31'
   page = requests.get(url, headers=headers)
   if not page.status_code == 200:
      raise RuntimeError()
   soup = BeautifulSoup(page.content, 'html.parser')
   elems = soup.find_all(class_="entry-title td-module-title")
   items = [elem_to_item(elem.findChildren('a')[0]) for elem in elems]
   feed = Feed(title="Smart Cities", link=url, language="en", lastBuildDate=now, items=items)
   with open('rss/smart_cities.xml', 'w') as file:
      file.write(feed.rss())

def smart_grid():
   url = 'https://www.smart-energy.com/?s=&doubleFilter=true&blockID=107975&categoryOne=716&categoryTwo=31'
   page = requests.get(url, headers=headers)
   if not page.status_code == 200:
      raise RuntimeError()
   soup = BeautifulSoup(page.content, 'html.parser')
   elems = soup.find_all(class_="entry-title td-module-title")
   items = [elem_to_item(elem.findChildren('a')[0]) for elem in elems]
   feed = Feed(title="Smart Grid", link=url, language="en", lastBuildDate=now, items=items)
   with open('rss/smart_grid.xml', 'w') as file:
      file.write(feed.rss())