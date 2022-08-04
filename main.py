from webscraper import *

scrapers = [smart_cities, smart_grid]
for scrape in scrapers:
   try:
      scrape()
   except Error:
      pass