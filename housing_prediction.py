from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.rew.ca/properties/areas/vancouver-bc')
soup = BeautifulSoup(html_text, 'lxml')
house = soup.find_all('div', class_ = 'col-xs-12 col=md=8').text
print(soup.prettify())






## Price, Neighborhood, City, Bedrooms, Bathrooms, Square Feet
## Dimension Hierachy: City -> Neighborhood
# Fact tables: Price
# Rolling append for amount of data inputted
