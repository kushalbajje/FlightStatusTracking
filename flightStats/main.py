#########------------------flightStats---------------------------########

import self as self
import unittest
from selenium import webdriver
import pandas
import json
from selenium.webdriver.common.keys import Keys
import re
import time

lst = []
lst1 = []


#######-----------------------Setting the path for chromedriver-------------######
driver = webdriver.Chrome(executable_path="D:\\chromedriver_win32\\chromedriver.exe")

#######---------------------------opening url---------------------------#######
driver.get("https://www.flightstats.com/v2/")

flightNo = input("Enter flight number")

#####-------------splitting up flight name and number---------#############
temp = re.compile("([a-zA-Z]+)([0-9]+)")
res = temp.match(flightNo).groups()


airLine = res[0]
flightNumber = res[1]
###------------to fetch data--------------#####
try:
    input_element = driver.find_element_by_xpath(".//*[@class='flight-tracker-adv-search-button']").click()
    element1 = driver.find_element_by_xpath(".//*[@class='async-common__StyledInput-s6djn13-0 hgDxUM']")
    element1.send_keys(airLine)
    time.sleep(8)
    element1.send_keys(Keys.ARROW_DOWN)
    element1.send_keys(Keys.RETURN)
    element2 = driver.find_element_by_xpath(".//*[@class='basic-text__StyledInput-s11k2oyc-1 sOmGX']")
    element2.send_keys(flightNumber)
    element3 = driver.find_element_by_xpath(".//*[@class='basic-button__Button-s3qdr1i-0 jIURFr']").click()

    time.sleep(8)



    for element in driver.find_elements_by_class_name("ticket__TicketContainer-s1rrbl5o-0.bgrndo"):
        lst.append(element.text)
    lst1 = lst[0].splitlines()
    data = {
        "flightNumber":lst1[0],
        "flightName":lst1[1],
        "flightStatus":lst1[6]+" "+lst1[7],
        "from":{
            "fromAirport" : lst1[2],
            "fromCity": lst1[3],
            "departureDate":lst1[11],
            "scheduled_DepartureTime":lst1[13],
            "actual_DepartureTime":lst1[15],
            "terminal":lst1[17],
            "gate":lst1[19],
        },
        "to":{
            "toAirport": lst1[4],
            "toCity": lst1[5],
            "arrivalDate":lst1[23],
            "scheduled_ArrivalTime":lst1[25],
            "actual_ArrivalTime":lst1[27],
            "terminal":lst1[29],
            "gate":lst1[31],
        }
    }
    json_format = json.dumps(data)
    print(json_format)

######-----if flight not found----------########
except:
    data1 = {
        "status":"Flight not found"
    }
    print(json.dumps(data1))

time.sleep(15)
driver.quit()