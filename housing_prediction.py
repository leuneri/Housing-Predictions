from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
import os
from tabulate import tabulate



def houseSearch():
    insertions = []
    count = 1
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
                insertion = (count, price, neighborhood, city, bedroom, bathroom, size)
                insertions.append(insertion)
                count += 1
                
            except:
                continue

    print(insertions)
    return insertions
    
    


if __name__ == "__main__":
    # while True:
    houseSearch()
#     print("Waiting for next cycle")
        # time.sleep(2678400) # 31 days


