from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.rew.ca/properties/areas/vancouver-bc')
soup = BeautifulSoup(html_text.text, 'lxml')
house = soup.find('div', class_ = 'displaypanel-content')
location = house.find('ul', class_ = "inlinelist displaypanel-info")
neighborhood = location.findAll("li")[0].text
city = location.findAll("li")[1].text
information = house.find('div', class_ = 'displaypanel-section clearfix')
bedrooms = information.findAll("li")[0].text
bathrooms = information.findAll("li")[1].text
squareFeet = information.findAll("li")[2].text
print(bedrooms)
print(bathrooms)
print(squareFeet)




## Price, Neighborhood, City, Bedrooms, Bathrooms, Square Feet
## Dimension Hierachy: City -> Neighborhood
# Fact tables: Price
# Rolling append for amount of data inputted
