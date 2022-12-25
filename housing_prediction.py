from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
import os
from tabulate import tabulate

def houseSearch():
    prices = []
    neighborhoods = []
    cities = []
    bedrooms = []
    bathrooms = []
    squareFeet = []
    for i in range(50):
        html_text = requests.get('https://www.rew.ca/properties/areas/greater-vancouver-bc/sort/latest/desc/page/{}?query=Greater+Vancouver%2C+BC'.format(i))
        soup = BeautifulSoup(html_text.text, 'lxml')
        houses = soup.findAll('div', class_ = 'displaypanel-content')
        for house in houses:
            try:
                price = house.find('div', class_ = "displaypanel-price hidden-xs").text
                location = house.find('ul', class_ = "inlinelist displaypanel-info")
                neighborhood = location.findAll("li")[0].text
                city = location.findAll("li")[1].text
                information = house.find('div', class_ = 'displaypanel-section clearfix')
                bedroom = information.findAll("li")[0].text
                bathroom = information.findAll("li")[1].text
                size = information.findAll("li")[2].text
                prices.append(price)
                neighborhoods.append(neighborhood)
                cities.append(city)
                bedrooms.append(bedroom)
                bathrooms.append(bathroom)
                squareFeet.append(size)
            except:
                continue

    dict = {'Price': prices, 'Neighbourhood': neighborhoods, 'City': cities, 'Bedrooms': bedrooms, 'Bathrooms': bathrooms, "Size (sq feet)": squareFeet}
    df = pd.DataFrame(dict)
    print(tabulate(df, headers = 'keys', tablefmt = 'psql'))
    df.to_csv(os.getcwd()+'\\outputs.csv')
    
    


if __name__ == "__main__":
    # while True:
    houseSearch()
    print("Waiting for next cycle")
        # time.sleep(2678400) # 31 days


## Price, Neighborhood, City, Bedrooms, Bathrooms, Square Feet
## Dimension Hierachy: City -> Neighborhood
# Fact tables: Price
# Rolling append for amount of data inputted
