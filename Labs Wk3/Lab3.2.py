# Paul Caulfield, 2020
import requests 
# Import Request Module
import csv
from bs4 import BeautifulSoup
# import Beautiful Soup package for navigating HTML & XML DOM trees, use to prettify 
with open("carviewer.html") as fp:
    # open file and send contents to Beautiful Soup as fp
    soup = BeautifulSoup(fp, 'html.parser')
    # parse the file and stores the DOM tree as 'soup'
#print(soup.prettify())
# print DOM tree
#print (soup.tr)
# print 1st occurrence of element which contains tr tagline
employee_file = open('week03data.csv', mode='w') 
# open file and name it 'employee.csv and set the file mode = w for write - to create blank csv file
employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
# make virable called employee.writer which uses csv writer to write to (filename,delimite and other paramters)



rows = soup.findAll("tr")
# return a list of elements with tr tagline and sore in memory
for row in rows:
    #iterate through rows  
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
    employee_writer.writerow(dataList)
    # to write row, pass list  

#listings = soup.findAll("table", class_="table" )

#for listing in listings:
#    entryList = []
    
#    reg = listing.find(th="Reg").text
#    entryList.append(reg)
#    make = listing.find(th="Make").text
#    entryList.append(make)
#    model = listing.find(th="Model").text
#    entryList.append(model)
#   price = listing.find(th="Price").text
#    entryList.append(price)

#   employee_writer.writerow(entryList)

    