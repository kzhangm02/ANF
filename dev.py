import requests
from bs4 import BeautifulSoup
from xml.dom import minidom
from rfeed import *
import datetime

def elem_to_item(elem):
   title = elem.get_text()
   link = elem.get('href')
   return Item(title=title, link=link)

headers = {'User-Agent': 'Chrome/103.0.0.0'}
url = 'https://www.smart-energy.com/?s=&doubleFilter=true&blockID=107975&categoryOne=9897&categoryTwo=35'
page = requests.get(url, headers=headers)
if not page.status_code == 200:
   sys.exit(f'Error {page.status_code}')
   
soup = BeautifulSoup(page.content, 'html.parser')
elems = soup.find_all(class_="entry-title td-module-title")
items = [elem_to_item(elem.findChildren('a')[0]) for elem in elems]
feed = Feed(title="My RSS",
            link="https://www.google.com",
            language="en",
            lastBuildDate=datetime.datetime.now(),
            items=items)
with open('test.xml', 'w') as f:
   f.write(feed.rss())