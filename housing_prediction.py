from bs4 import BeautifulSoup
import requests
import time

def houseSearch():
    for i in range(100):
        try:
            html_text = requests.get('https://www.rew.ca/properties/areas/vancouver-bc/sort/latest/desc/page/{}?query=Vancouver%2C+BC'.format(i))
            soup = BeautifulSoup(html_text.text, 'lxml')
            houses = soup.findAll('div', class_ = 'displaypanel-content')
            for house in houses:
                try:
                    price = house.find('div', class_ = "displaypanel-price hidden-xs").text
                    location = house.find('ul', class_ = "inlinelist displaypanel-info")
                    neighborhood = location.findAll("li")[0].text
                    city = location.findAll("li")[1].text
                    information = house.find('div', class_ = 'displaypanel-section clearfix')
                    bedrooms = information.findAll("li")[0].text
                    bathrooms = information.findAll("li")[1].text
                    squareFeet = information.findAll("li")[2].text
                    print(price)
                    print(neighborhood)
                    print(city)
                    print(bedrooms)
                    print(bathrooms)
                    print(squareFeet)
                except:
                    print("MISSING INFORMATION")
        except:
            break
    

if __name__ == "__main__":
    while True:
        houseSearch()
        print("Waiting for next cycle")
        time.sleep(2678400) # 31 days


## Price, Neighborhood, City, Bedrooms, Bathrooms, Square Feet
## Dimension Hierachy: City -> Neighborhood
# Fact tables: Price
# Rolling append for amount of data inputted
