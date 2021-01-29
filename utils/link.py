"""
    This module provides a tool to get a list of urls to send requests to.

    It was added at the end of the project to replace a hardcoded list of
    url's in the main.py file. There, the list of url's is used as targets
    to scrape data from.

    The module has only one class ZimmoLinks, which has one method generate()
    that can be used to generate a list of urls to scrape data from.

    The generate() method contains procedural code and is only intended to
    demonstrate that links can be scraped if only one request is sent per
    minute.
"""

import random
import requests
import time

from bs4 import BeautifulSoup

class ZimmoLinks():
    """ This is a tool to generate a list of zimmo.be urls.

        Notes:
        - Each url points to the page with the property's data.
        - You should pass a "page to start from" and a "number of pages".
        - The code is slow. After every request, minimum 60 sec pauze.
    """

    def __init__(self, number_of_pages, start_page):
        self.number_of_pages = number_of_pages
        self.start_page = start_page
        self.urls = []


    def generate(self):
        """ Procedure to generate a list of zimmo urls to use for scraping.

            Disclaimer:
            This method is one giant, cleaned up copy-paste from jupyter notebook
            because out of time to build something better.
        """

        # set the url pattern to generate urls
        url = "https://www.zimmo.be/nl/panden/?status=1&type[0]=5&type[1]=1&region=none&pagina={page_number}"

        # set a headers dictionary for the http get request (mimics a browser)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0"
        }

        # configure the range of pages
        page_to_start_at = self.start_page
        pages_to_request = self.number_of_pages

        # calculate a range of page numbers to request
        end_of_range = page_to_start_at + pages_to_request
        page_numbers = range(page_to_start_at, end_of_range)

        # configure a time interval
        minimal_request_interval = 60  # estimate of acceptable robot behaviour

        # create a loop that will request the pages
        # note 1: to avoid getting banned, implement a timer to slow down requests
        # note 2: to avoid getting banned, set a user agent for the requests to mimic browser requests

        request_url = ""
        html_responses = []

        for page_number in page_numbers:

            # first construct the url
            request_url = url.format(page_number = page_number)

            # then get request & append to list
            response = requests.get(request_url, headers = headers)
            html_responses.append(response.text)

            # now slow down the loop

            # add a random float between 0 and 1 to the configured minimum interval
            request_interval = minimal_request_interval + random.random()

            # pauze unless it's the last page
            if page_number != page_numbers[-1]:
                time.sleep(request_interval)

        # parse html and extract links
        for html in html_responses:
            soup = BeautifulSoup(html, 'html')

            for elem in soup.find_all('a',attrs={"property-item_link"}):
                self.urls.append(elem.get('href'))

        return self.urls
