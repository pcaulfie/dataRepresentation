# Paul Caulfield, 2020
# Write a program that stores the data for all trains in Ireland in a csv file
# Use the Irish rail API http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML to retrieve the data.
import requests 
# Import Request Module
import csv
from bs4 import BeautifulSoup
# import Beautiful Soup package for navigating HTML & XML DOM trees, use to prettify 
url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
# url = Irish rail API
page = requests.get(url)
# use requests.get to pass url
soup = BeautifulSoup(page.content, 'xml')
# parse the file using xml parser as API is in XML and stores the DOM tree as 'soup'
# print(soup.prettify()) 
retrieveTags=['TrainStatus', 'TrainLatitude', 'TrainLongitude', 'TrainCode', 'TrainDate', 'PublicMessage', 'Direction' ]

with open('week03_train.csv', mode='w') as train_file: 
# open csv file
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    listings = soup.findAll("objTrainPositions") 
    # find the listings ie all elements = objTrainPositions
    for listing in listings: 
    # iterate through the listing in order to print each out
        lat =float( listing.TrainLatitude.string) 
        #get the latitude of this train and store it as a float
        if (lat < 53.4):
        # then check if it is less then the latitude of Dublin 53.4
            #print(listing)
            #print(listing.TrainLatitude.string)
            #print(listing.find('TrainLatitude').string)
            # print the content of the element TrainLatitude
            entryList = [] 
            # create an array called entryList
            for retrieveTag in retrieveTags:
            #for loop to iterate through these tag names.
                #print (listing.find(retrieveTag).string) 
                entryList.append(listing.find(retrieveTag).string)
                #append in the latitude.
                train_writer.writerow(entryList)
                # write data to the CSV.

train_file.close()
# close file