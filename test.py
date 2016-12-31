# from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from selenium.webdriver.common.keys import Keys

# import data

# iterations = 10

# data = data.DataCsv("test.csv",' ', '|')
# data.set_classifiers()
# print(data.get_rows())

# caps = DesiredCapabilities.FIREFOX

# caps["marionette"] = True

# caps["binary"] = "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"
    
# driver = webdriver.Firefox(capabilities=caps)
# driver.get('C:\\Users\\CalebsComp\\Documents\\homeworkSolver\\sample\\main.html')


# for i in range(0,iterations):

#     elem = driver.find_element_by_id('prompt')
#     print(elem.text)

#     elem = driver.find_element_by_id('inputBox')
#     elem.send_keys('16');

x #     elem = driver.find_element_by_id('inputButton')
#     elem.click()
#     driver.refresh()
#https://github.com/SeleniumHQ/selenium/blob/master/py/selenium/webdriver/remote/webelement.py

import browser
import data

# test pls ignore
def main():
    browser2 = browser.Browser('C:\\Users\\CalebsComp\\Documents\\homeworkSolver\\sample\\main.html',10)
    data2 = data.DataCsv("test.csv",' ','|')
    def f():
        l = list() 
        
        prompt = browser2.find_elem('prompt')
        l.append(prompt.text)
        
        input_box = browser2.find_elem('inputBox')
        input_box.send_keys('100')
        l.append('100')
        
        input_button = browser2.find_elem('inputButton')
        input_button.click()

        answer_label = browser2.find_elem('passLabel')
        l.append(answer_label.text)

        print(l)
        data2.write_new_row(l)
        browser2.refresh_browser()
    
    browser2.process(f)
    print(data2.get_rows())
    data2.set_classifiers()
    
if __name__ == '__main__':
    main()
