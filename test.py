from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys

import data

data = data.DataCsv("iris.csv",' ', '|')
#data.write_new_row(['1','1','1','1'])
#data.label_classifiers()
print(data.get_rows())

# caps = DesiredCapabilities.FIREFOX

# caps["marionette"] = True

# caps["binary"] = "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"

# driver = webdriver.Firefox(capabilities=caps)
# driver.get('C:\\Users\\CalebsComp\\Documents\\homeworkSolver\\sample\\main.html')

# elem = driver.find_element_by_id('prompt')
# print(elem.text)

# elem = driver.find_element_by_id('inputBox')
# elem.send_keys('16');

# elem = driver.find_element_by_id('inputButton')
# elem.click()
#https://github.com/SeleniumHQ/selenium/blob/master/py/selenium/webdriver/remote/webelement.py

