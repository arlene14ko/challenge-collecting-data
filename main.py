#importing the needed packages
import pandas as pd

from utils.link import ZimmoLinks
from utils.requests import RequestData

urls = ("https://www.zimmo.be/nl/panden/?status=1&type%5B0%5D=5&type%5B1%5D=1&type%5B2%5D=4&type%5B3%5D=3&type%5B4%5D=2&type%5B5%5D=6&hash=be88f65d166369a3006e8c0c11674f3b&priceIncludeUnknown=1&priceChangedOnly=0&bedroomsIncludeUnknown=1&bathroomsIncludeUnknown=1&constructionIncludeUnknown=1&livingAreaIncludeUnknown=1&landAreaIncludeUnknown=1&commercialAreaIncludeUnknown=1&yearOfConstructionIncludeUnknown=1&epcIncludeUnknown=1&queryCondition=and&includeNoPhotos=1&includeNoAddress=1&onlyRecent=0&onlyRecentlyUpdated=0&isPlus=0&excludedEstates%5B0%5D=JIK92&excludedEstates%5B1%5D=JLAKQ&excludedEstates%5B2%5D=JRA1O&excludedEstates%5B3%5D=JRU4B&region=list&city=MwQA&pagina=10#gallery",
        "https://www.zimmo.be/nl/panden/?status=1&type%5B0%5D=5&type%5B1%5D=1&type%5B2%5D=4&type%5B3%5D=3&type%5B4%5D=2&type%5B5%5D=6&hash=be88f65d166369a3006e8c0c11674f3b&priceIncludeUnknown=1&priceChangedOnly=0&bedroomsIncludeUnknown=1&bathroomsIncludeUnknown=1&constructionIncludeUnknown=1&livingAreaIncludeUnknown=1&landAreaIncludeUnknown=1&commercialAreaIncludeUnknown=1&yearOfConstructionIncludeUnknown=1&epcIncludeUnknown=1&queryCondition=and&includeNoPhotos=1&includeNoAddress=1&onlyRecent=0&onlyRecentlyUpdated=0&isPlus=0&excludedEstates%5B0%5D=JIK92&excludedEstates%5B1%5D=JLAKQ&excludedEstates%5B2%5D=JRA1O&excludedEstates%5B3%5D=JRU4B&region=list&city=MwQA&pagina=9#gallery",
        "https://www.zimmo.be/nl/panden/?status=1&type%5B0%5D=5&type%5B1%5D=1&type%5B2%5D=4&type%5B3%5D=3&type%5B4%5D=2&type%5B5%5D=6&hash=be88f65d166369a3006e8c0c11674f3b&priceIncludeUnknown=1&priceChangedOnly=0&bedroomsIncludeUnknown=1&bathroomsIncludeUnknown=1&constructionIncludeUnknown=1&livingAreaIncludeUnknown=1&landAreaIncludeUnknown=1&commercialAreaIncludeUnknown=1&yearOfConstructionIncludeUnknown=1&epcIncludeUnknown=1&queryCondition=and&includeNoPhotos=1&includeNoAddress=1&onlyRecent=0&onlyRecentlyUpdated=0&isPlus=0&excludedEstates%5B0%5D=JIK92&excludedEstates%5B1%5D=JLAKQ&excludedEstates%5B2%5D=JRA1O&excludedEstates%5B3%5D=JRU4B&region=list&city=MwQA&pagina=8#gallery")

start_page = 1
number_of_pages = 10  # 1 request/minute, so this is also approximately the execution time in minutes

for url in urls:
    df = RequestData.start_scrapping(url)
    if url == urls[0]:
        df.to_csv('data/zimmo_data.csv', index=False)
    else:
        df.to_csv('data/zimmo_data.csv', mode='a', header=False, index=False)

print("Data scrapping successful!")
