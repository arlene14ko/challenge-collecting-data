# Collecting Data Challenge

- Developer Names : `Joren Vervoort, Philippe Planchar, and Arlene Postrado` 
- Level: `Junior Developer`
- Started: `27/01/2021 H:9h00`
- Duration: `3 days`
- Deadline: `29/01/2021 H:16h00`
- Team challenge : `Group of 3`
- Type of Challenge: `Consolidation`
- Promotion: `AI Theano 2`
- Coding Bootcamp: `Becode  Artificial Intelligence (AI) Bootcamp`

## Goal Objective

To create a a Python program using the Python library to collect as much data as possible. 

## Learning Objectives
- To be be able to scrape a website
- To be able to build a dataset from scratch
- To be able to Implement a strategy to collect as much data as possible.
- Having a clean architecture
- Be able to go deeper in object inheritance
- Improve in using classes

## About the Repository

By scraping the real estate website https://www.zimmo.be/nl/, a dataset of at least 10.000 properties in Belgium will be
created. This overview will be available in the included csv file.

### Repository

**README.md**

**main.py**
  - this is where you start the program
  - everything that you need to start scrapping is imported here 
  
**utils folder**
  - this has 3 files namely:
      1. **requests.py**
          - this is where you get the requests for the data, we used Beautiful Soup to get the data from the website.
          - the data is then cleaned and put in a dictionairy.
          
      2. **getting_data.py**
          - this is where we convert the cleaned data that we got from requests.py and save it in a dataframe using pandas
      
**data folder**
  - this contains 1 csv file:
      1. **ZimmoData.csv**
          - this is where the data is saved, it is in a csv format
          
### Project Status

The progamm is running and works. An overview of the collected data can be found in the csv file. But due to limited time, the minimum data of 10.000 properties could not be achieved. To achieve this goal the program should run for approximatly 3 days straight. 

  
### Thank you for reading.
