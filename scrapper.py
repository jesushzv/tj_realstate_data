# -*- coding: utf-8 -*-
from stripAccents import strip_accents
from getCoordenates import getCoordenates

from selenium import webdriver
from time import sleep
import csv


driver = webdriver.Chrome('/Users/jzamora2/Downloads/chromedriver')
driver.implicitly_wait(10)

#Store all
master = []

#Function that will scrap data from a single page
def scrapper(url):
    # Array to store all of the properties
    properties = []

    # Format of each property
    property = {
        'price': None,
        'currency': None,
        'bedrooms': None,
        'bathrooms': None,
        'parkingSpots': None,
        'propertySize': None,
        'neighborhood': None,
        'lat': None,
        'lon': None
    }

    driver.get(url)
    sleep(4)

    try:
        driver.find_element_by_class_name("mdl-close-btn").click()
    except:
        pass

    # Select the houses
    houses = driver.find_elements_by_class_name("postingCardInfo")

    # Select only the first one for testing purpurses
    for test in houses:
        dummy = dict(property)

        # currency and price

        try:

            priceInfo = test.find_element_by_class_name("firstPrice").text.split(' ')

            price = priceInfo[1]
            price = price.replace(',', '')

            dummy['price'] = price
            dummy['currency'] = priceInfo[0]

        except:
            pass

        # Group the main features
        e = test.find_element_by_class_name("postingCardMainFeatures").find_elements_by_tag_name("li")

        # Property size
        try:
            propertySize = e[0].text
            propertySize = propertySize.split(' ')[0]
            dummy['propertySize'] = int(propertySize)
        except:
            pass

        # Bedrooms

        try:
            bedrooms = e[1].text
            bedrooms = bedrooms.split(' ')[0]
            dummy['bedrooms'] = int(bedrooms)
        except:
            pass

        try:
            bathrooms = e[2].text
            bathrooms = bathrooms.split(' ')[0]
            dummy['bathrooms'] = int(bathrooms)

        except:
            pass


        try:
            parkingSpots = e[3].text
            parkingSpots = parkingSpots.split(' ')[0]
            dummy['parkingSpots'] = int(parkingSpots)
        except:
            pass

        try:
            neighborhood = test.find_element_by_class_name('postingCardLocation').find_element_by_tag_name("span").text
            dummy['neighborhood'] = neighborhood
        except :
            pass

        
        coordenates = getCoordenates(dummy['neighborhood'])

        dummy['lat'] = coordenates[0]
        dummy['lon'] = coordenates[1]
        
        properties.append(dummy)

    return properties



master += scrapper("https://www.inmuebles24.com/casas-en-venta-en-tijuana.html")

driver.close()

for i in range(2,38):
    driver = webdriver.Chrome('/Users/jzamora2/Downloads/chromedriver')
    driver.implicitly_wait(8)

    url = ("https://www.inmuebles24.com/casas-en-venta-en-tijuana-pagina-%s.html" % i)
    
    sleep(4)
    
    master += scrapper(url)
    driver.close()

with open('data.csv','w',) as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['price','currency','bedrooms','bathrooms','parkingSpots','propertySize','neighborhood','lat','lon'])
    for house in master:
        writer.writerow([strip_accents(e) for e in [house['price'],house['currency'],house['bedrooms'],house['bathrooms'],house['parkingSpots'],house['propertySize'],house['neighborhood'],house['lat'],house['lon']]])




