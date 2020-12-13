#########-------------------------flightAware----------------------###########

from selenium import webdriver
import json
import time

lst = []
lst1 = []
lst2 = []
lst3 = []

########------------------------setting path for chromedriver----------------########
driver = webdriver.Chrome(executable_path="D:\\chromedriver_win32\\chromedriver.exe")

########----------------------------opening url-----------------------------########
driver.get("http://www.flightaware.com/")
flightNo = input("Enter flight number")

########------------------to fetch data----------------------------###########
try:
    input_element = driver.find_element_by_id("s2id_autogen1")
    input_element.send_keys(flightNo)
    driver.find_element_by_class_name('orange_button').click()
    time.sleep(10)
    for element in driver.find_elements_by_class_name('flightPageSummary '):
        lst2.append(element.text)
    lst3 = lst2[0].splitlines()
    for element in driver.find_elements_by_id('flightPageTourStep1'):
        lst.append(element.text)
    lst1 = lst[0].splitlines()
    if len(lst1) == 20:
        data = {
            "flightNumber":lst3[1],
            "flightName":lst3[0],
            "flightStatus":lst3[3]+" "+lst3[4],
            "from":{
                "fromAirport" : lst1[0],
               "fromCity": lst1[1],
               "departureDate":lst1[8],
               "departureTime":lst1[9],
               "terminal":lst1[4],
               "startStatus":lst1[10]
            },
            "to":{
                "toAirport" : lst1[2],
                "toCity": lst1[3],
                "arrivalDate":lst1[11],
                "arrivalTime":lst1[12],
                "landingStatus":lst1[13]
            },
            "totalTime": lst1[16],
            "timeRemaining": lst1[17],
            "timeElapsed": lst1[15],
            "milesCovered": lst1[18],
            "milesLeft": lst1[19]
        }
    #########-------------Flight in halt--------------######
    else:
        data = {
            "flightNumber":lst3[1],
            "flightName":lst3[0],
            "flightStatus":lst3[3]+" "+lst3[4],
            "from": {
                "fromAirport": lst1[0],
                "fromCity": lst1[1],
                "departureDate": lst1[8],
                "departureTime": lst1[9],
                "terminal": lst1[4],
                "startStatus": lst1[10]
            },
            "to": {
                "toAirport": lst1[2],
                "toCity": lst1[3],
                "arrivalDate": lst1[11],
                "arrivalTime": lst1[12],
                "landingStatus": lst1[13]
            },
            "totalTime": lst1[14]
        }

    json_format = json.dumps(data)
    print(json_format)

#######---------------if flight not found------------------#########
except:
    data1 = {
        "status":"Flight not found"
    }
    print(json.dumps(data1))

time.sleep(15)
driver.quit()