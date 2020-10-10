# Paul Caulfield, 2020
from bs4 import BeautifulSoup
# import Beautiful Soup package for navigating HTML & XML DOM trees, use to prettify 
with open("../carviewer.html") as fp:
    # open file and send contents to Beautiful Soup as fp
    soup = BeautifulSoup(fp, 'html.parser')
    # parse the file and stores the DOM tree as 'soup'
#print(soup.prettify())
# print DOM tree
#print (soup.tr)
# print 1st occurrence of element which contains tr tagline
rows = soup.findAll("tr")
# return a list of elements with tr tagline and sore in memory
for row in rows:
#   iterate through rows  
    #print(row)
    # print rows
    dataList = []
    # create an array call dataList 
    cols = row.findAll("td")
    # return a list of elements with td tagline and sore in cols

    for col in cols:
    # iterate through cols
        dataList.append(col.text)
        # append text element into array dataList
    print(dataList)
    #print array