import datetime
from webscrapers import *

now = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")
scrapers = [smart_cities, smart_grid]
status = f'Status Report\n{now}\n\n'
for scraper in scrapers:
   name = " ".join(scraper.__name__.upper().split("_"))
   try:
      scraper()
      status += f'{name}: SUCCESS\n'
   except RuntimeError:
      status += f'{name}: FAIL\n'
with open('./status.txt', 'w') as file:
   file.write(status)   