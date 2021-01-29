from bs4 import BeautifulSoup
import requests
import time

#importing gettingdata.py
from utils.getting_data import GettingData

class RequestData:
    
    
    def start_scrapping(url):
        #get data from Beautiful Soup
        soup = RequestData.request_website(url)
        
        #getting the links in the main page
        links = RequestData.get_links(soup)
        
        properties = []
        #requesting data for each link in the list of links
        #using a loop to get all the data
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
            
            dict_elem = RequestData.clean_data(keys, values)
            details = GettingData.getting_data(dict_elem)
            print(details)
            
            properties.append(details)
            
        
        data = GettingData.convert_to_csv(properties)
        
        #success = print("Congratulations! Getting data successful!")
        return(data)
         
    def request_website(url):
        #requesting data using beautiful soup
        time.sleep(10)
        r = requests.get(url)
        print(url, r.status_code)
        time.sleep(10)
        soup = BeautifulSoup(r.text,'html') #lxml
        return soup
    
    
    def get_links(soup):
        #getting the links in a list
        link = []
        for elem in soup.find_all('a',attrs={"property-item_link"}):
            link.append(elem.get('href'))
        
        #updating the links in the correct format
        links = ['https://zimmo.be'+ elem for elem in link]
        return links
    
    
    def clean_data(keys, values):
        #cleaning the datas and putting it to a list
        clean_keys = []
        for k in (keys):
            clean_keys.append(k.strip())
        
        clean_values = []
        for v in (values):
            clean_values.append(v.strip())
            
        #putting the key and value to a dictionary
        dict_elements = {}
        for key,value in zip(clean_keys, clean_values):
            dict_elements[key] = value
        
        return dict_elements
            
        
                
                
                    
            
            

