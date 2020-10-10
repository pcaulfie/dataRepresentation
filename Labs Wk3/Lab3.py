# Paul Caulfield, 2020
# Getting Content Into Program
import requests 
# Import Request Module
from bs4 import BeautifulSoup
# import Beautiful Soup package for navigating HTML & XML DOM trees, use to prettify 
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
# use requests.get to pass url
soup1 = BeautifulSoup(page.content, 'html.parser')
print(page)
# PPrint page
print("----------------")
#print(page.content)
# Print content
print(soup1.prettify())