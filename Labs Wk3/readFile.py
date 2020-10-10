# Paul Caulfield, 2020
# Import Request Module
from bs4 import BeautifulSoup
# import Beautiful Soup package for navigating HTML & XML DOM trees, use to prettify 
with open("../carviewer.html") as fp:
    # open file and send contents to Beautiful Soup as fp
    soup = BeautifulSoup(fp, 'html.parser')
    # parse the file and stores the DOM tree as 'soup'
print(soup.prettify())
# print DOM tree