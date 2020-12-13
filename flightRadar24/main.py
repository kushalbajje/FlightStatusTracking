#-----flightRadar24-----#
from selenium import webdriver
import json
from selenium.webdriver.common.keys import Keys
import time


lst = []
lst1 = []
lst2 = []
lst3 = []

#########---------------- Setting the path for chrome Driver---------------------------########
driver = webdriver.Chrome(executable_path="D:\\chromedriver_win32\\chromedriver.exe")

########------------------- opening url ---------------------------------------#########
driver.get("https://www.flightradar24.com/")


flightNo = input("Enter flight number")

#----------to fetch data---------#
input_element = driver.find_element_by_id("searchBox")
input_element.send_keys(flightNo)
time.sleep(2)

try:
    input_element.send_keys(Keys.ARROW_DOWN)
    input_element.send_keys(Keys.ARROW_DOWN)
    time.sleep(2)
    element1 = driver.find_element_by_class_name("rowButton.goto").click()
    time.sleep(3)
    for flightName in driver.find_elements_by_class_name("pnl-component.airline-info.appear"):
        lst2.append(flightName.text)
    lst3 = lst2[0].splitlines()
    for elements in driver.find_elements_by_class_name("scroll-wrapper"):
        lst.append(elements.text)
    lst1 = lst[0].splitlines()
    data = {

        "flightNumber": lst3[0],
        "flightName": lst3[1],
        "from": {
            "fromAirport": lst1[0],
            "fromCity": lst1[1],
            "scheduled_DepartureTime": lst1[4],
            "actual_DepartureTime": lst1[6]
        },
        "to": {
            "toAirport": lst1[7],
            "toCity": lst1[8],
            "scheduled_ArrivalTime": lst1[11],
            "actual_ArrivalTime": lst1[13]
        },
        "distanceTravelled": lst1[14],
        "distanceLeft": lst1[15]

    }
    json_format = json.dumps(data)
    print(json_format)
#------if flight not found-------#
except:
    data1 = {
        "status": "Flight not found"
    }
    print(json.dumps(data1))
time.sleep(15)
driver.quit()
