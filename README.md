### Automated News Feed for Asian Americans in Energy, the Environment, and Commerce (AE2C)

The webscraper currently creates RSS feeds for these topics:
 - Smart cities
 - Smart grid

Topics to be added in the future:
 - TBD

### Structure
 - [`.github/workflows/automate.yml`](./.github/workflows/automate.yml): This file controls script automation and updates the RSS feeds. It currently runs daily at 10 AM but may be configured to any set schedule using cron jobs. The repository owner's email must be included in the global Git configuration field.
 - [`feeds`](./feeds): This directory includes all the RSS feeds for each topic (i.e. one distinct page in the news feed) as .xml files. The files are hosted on GitHub at https://*OWNER_USERNAME*.github.io/ANF/feeds/*FILE_NAME*.xml
 - [`scrape`](./scrape): This directory includes all the code to generate the RSS feeds and the status reports.
   - [`main.py`](./scrape/main.py): This file runs all the scraper functions in webscraper.py and creates the status report.
   - [`utils.py`](./scrape/utils.py): This file contains formatting functions to generate the RSS feeds. Most of the functions are not relevant, only the `Item` and `Feed` classes are useful.
   - [`webscrapers.py`](./scrape/webscrapers.py): This file contains the webscraper functions to extract articles from websites and convert them into RSS feeds.
 - [`status.txt`](./status.txt): Displays the SUCCESS or FAIL status of each RSS feed after the most recent update.
 
 ### Pipeline for creating a news feed
 1. Create a new function in [`webscrapers.py`](./scrape/webscrapers.py) which extracts articles from the desired website and converts them to RSS format.
 2. Add the function name (without parenthesis) to the `scrapers` list in [`main.py`](./scrape/main.py).
 3. Create a news feed on the AE2C website which points to the link where GitHub hosts the new RSS feed.
