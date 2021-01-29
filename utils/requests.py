# Importing the necessary packages
from bs4 import BeautifulSoup
import requests
import time
from typing import List, Dict

#importing gettingdata.py
from utils.getting_data import GettingData


class RequestData:

    
    def start_scrapping(url: str):
        """
        Function that will start the program
        :attrib soup will contain the request_website function 
        :attrib link will contain the get_links function
        :attrib properties - starting with empty list, 
            - will contain a list of details of the properties
        :attrib data call the function convert_to_csv which will then be returned
        """
        soup = RequestData.request_website(url)
        
        links = RequestData.get_links(soup)
     
        """
        The loop will iterate to the list of links 
        :attrib url will contain the link
        :attrib soup will be the request_website function
        :attrib keys will contain the soup element (feature-label) 
        :attrib values will contain the soup element (feature-value)
        :attrib dict_elem will be a dict with keys, and values
            - it will also call the clean_data function that will clean the 
                keys and values data
        :attrib details will call the getting_data function 
            - it will contain the details per property
        Then the details will be appended to the property 
        """
        properties = []
        for link in links:
            url = link 
            soup = RequestData.request_website(url)
            
            keys = []
            for elem in soup.find_all('strong',attrs={"feature-label"}): 
                time.sleep(3)
                keys.append(elem.text)
            
            values = []
            for elem in soup.find_all('span',attrs={'feature-value'}): 
                time.sleep(3)
                values.append(elem.text)
            
            dict_elements = RequestData.clean_data(keys, values)
            details = GettingData.getting_data(dict_elements)
            print(details)
            
            properties.append(details)
        
        data = GettingData.convert_to_csv(properties)
        return(data)
         
    
    def request_website(url: str):
        """
        Function that will request the website details
        Added a time sleep 10 secs to avoid the captcha
        :attrib r will be the requests.get from the url
        :attrib soup will contain the html from Beautiful soup
        This function will return the attrib soup
        """
        time.sleep(10)
        r = requests.get(url)
        print(url, r.status_code)
        time.sleep(10)
        soup = BeautifulSoup(r.text,'html') #lxml
        return soup
    
    
    def get_links(soup) -> List(str):
        """
        Function that will get the attrib soup and scrape all the links in a link
        :attrib link will contain all the links, it will start as an empty list
        :attrib links will convert all the links to the correct format
        In this case, it is `https://zimmo.be` because we are currently using 
        this code for Zimmo website. If you are going to use it for another website
        Just change the link on the code. 
        This function will return the attrib links in a list format
        """
        link = []
        for elem in soup.find_all('a',attrs={"property-item_link"}):
            link.append(elem.get('href'))
        
        links = ['https://zimmo.be'+ elem for elem in link]
        return links
    
    
    def clean_data(keys: List(str), values: List(str)) -> Dict[str, str]:
        """
        Function that will has two parameters keys, and values
        This function will remove all the unnecessary characters on the data 
        and convert the keys, and values to a dictionary
        :attrib clean_keys will contain the cleaned keys list
        :attrib clean_values will contain the cleaned values list
        :attrib dict_elements will contain the dict of clean_keys and clean_values
        This function will return the attrib dict_elements in a dictionary format
        """
        clean_keys = []
        for k in (keys):
            clean_keys.append(k.strip())
        
        clean_values = []
        for v in (values):
            clean_values.append(v.strip())
            
        dict_elements = {}
        for key,value in zip(clean_keys, clean_values):
            dict_elements[key] = value
        
        return dict_elements
            
        
                
                
                    
            
            

