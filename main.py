#importing the needed packages
import pandas as pd

from utils.link import ZimmoLinks
from utils.requests import RequestData

number_of_pages = 10  # the search pages to scrape links from; e.g.: 10 => 210 links
start_page = 1

zlinks = ZimmoLinks(number_of_pages = number_of_pages, start_page = start_page)

urls = zlinks.generate()  # request 1 page/minute, so runs slowly

for url in urls:
    df = RequestData.start_scrapping(url)
    if url == urls[0]:
        df.to_csv('data/zimmo_data.csv', index=False)
    else:
        df.to_csv('data/zimmo_data.csv', mode='a', header=False, index=False)

print("Data scrapping successful!")
