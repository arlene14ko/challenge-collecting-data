#importing the needed packages
import pandas as pd

from utils.link import ZimmoLinks
from utils.requests import RequestData

""" commented, because replaced by link.py > ZimmoLinks class > generate()
urls = ("https://www.zimmo.be/nl/panden/?status=1&type%5B0%5D=5&type%5B1%5D=1&type%5B2%5D=6&hash=42e417545705ecaf4dec11fcf5f4b6bc&priceIncludeUnknown=1&priceChangedOnly=0&bedroomsIncludeUnknown=1&bathroomsIncludeUnknown=1&constructionIncludeUnknown=1&livingAreaIncludeUnknown=1&landAreaIncludeUnknown=1&commercialAreaIncludeUnknown=1&yearOfConstructionIncludeUnknown=1&epcIncludeUnknown=1&queryCondition=and&includeNoPhotos=1&includeNoAddress=1&onlyRecent=0&onlyRecentlyUpdated=0&isPlus=0&region=circle&radius=2212.3937848383&lat=51.21403940314&lng=4.4131694673391#gallery",
        "https://www.zimmo.be/nl/panden/?status=1&type%5B0%5D=5&type%5B1%5D=1&type%5B2%5D=6&hash=42e417545705ecaf4dec11fcf5f4b6bc&priceIncludeUnknown=1&priceChangedOnly=0&bedroomsIncludeUnknown=1&bathroomsIncludeUnknown=1&constructionIncludeUnknown=1&livingAreaIncludeUnknown=1&landAreaIncludeUnknown=1&commercialAreaIncludeUnknown=1&yearOfConstructionIncludeUnknown=1&epcIncludeUnknown=1&queryCondition=and&includeNoPhotos=1&includeNoAddress=1&onlyRecent=0&onlyRecentlyUpdated=0&isPlus=0&excludedEstates%5B0%5D=ILV8F&excludedEstates%5B1%5D=JNWIZ&excludedEstates%5B2%5D=JQ8B4&excludedEstates%5B3%5D=JRV7D&region=circle&radius=2212.3937848383&lat=51.21403940314&lng=4.4131694673391&pagina=2#gallery",
        "https://www.zimmo.be/nl/panden/?status=1&type%5B0%5D=5&type%5B1%5D=1&type%5B2%5D=6&hash=42e417545705ecaf4dec11fcf5f4b6bc&priceIncludeUnknown=1&priceChangedOnly=0&bedroomsIncludeUnknown=1&bathroomsIncludeUnknown=1&constructionIncludeUnknown=1&livingAreaIncludeUnknown=1&landAreaIncludeUnknown=1&commercialAreaIncludeUnknown=1&yearOfConstructionIncludeUnknown=1&epcIncludeUnknown=1&queryCondition=and&includeNoPhotos=1&includeNoAddress=1&onlyRecent=0&onlyRecentlyUpdated=0&isPlus=0&excludedEstates%5B0%5D=ILV8F&excludedEstates%5B1%5D=JNWIZ&excludedEstates%5B2%5D=JQ8B4&excludedEstates%5B3%5D=JRV7D&region=circle&radius=2212.3937848383&lat=51.21403940314&lng=4.4131694673391&pagina=3#gallery",
        "https://www.zimmo.be/nl/panden/?status=1&type%5B0%5D=5&type%5B1%5D=1&type%5B2%5D=6&hash=42e417545705ecaf4dec11fcf5f4b6bc&priceIncludeUnknown=1&priceChangedOnly=0&bedroomsIncludeUnknown=1&bathroomsIncludeUnknown=1&constructionIncludeUnknown=1&livingAreaIncludeUnknown=1&landAreaIncludeUnknown=1&commercialAreaIncludeUnknown=1&yearOfConstructionIncludeUnknown=1&epcIncludeUnknown=1&queryCondition=and&includeNoPhotos=1&includeNoAddress=1&onlyRecent=0&onlyRecentlyUpdated=0&isPlus=0&excludedEstates%5B0%5D=ILV8F&excludedEstates%5B1%5D=JNWIZ&excludedEstates%5B2%5D=JQ8B4&excludedEstates%5B3%5D=JRV7D&region=circle&radius=2212.3937848383&lat=51.21403940314&lng=4.4131694673391&pagina=4#gallery",
        "https://www.zimmo.be/nl/panden/?status=1&type%5B0%5D=5&type%5B1%5D=1&type%5B2%5D=6&hash=42e417545705ecaf4dec11fcf5f4b6bc&priceIncludeUnknown=1&priceChangedOnly=0&bedroomsIncludeUnknown=1&bathroomsIncludeUnknown=1&constructionIncludeUnknown=1&livingAreaIncludeUnknown=1&landAreaIncludeUnknown=1&commercialAreaIncludeUnknown=1&yearOfConstructionIncludeUnknown=1&epcIncludeUnknown=1&queryCondition=and&includeNoPhotos=1&includeNoAddress=1&onlyRecent=0&onlyRecentlyUpdated=0&isPlus=0&excludedEstates%5B0%5D=ILV8F&excludedEstates%5B1%5D=JNWIZ&excludedEstates%5B2%5D=JQ8B4&excludedEstates%5B3%5D=JRV7D&region=circle&radius=2212.3937848383&lat=51.21403940314&lng=4.4131694673391&pagina=5#gallery")
"""

start_page = 1
number_of_pages = 10  # 1 request/minute, so this is also approximately the execution time in minutes

zlinks = ZimmoLinks(start_page = start_page, number_of_pages = number_of_pages)

urls = zlinks.generate()  # this can take a while to complete (1 req/min)

data = pd.DataFrame()
for url in urls:
    df = RequestData.start_scrapping(url)
    data.append(df)


data.to_csv('ZimmoData.csv', index=False)

print("Data scrapping successful!")
