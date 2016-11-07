from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys

class Browser(object):
    
    def __init__(self,resource,iterations):
        self.iterations = iterations
        self.firefox_path = "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"

        caps = DesiredCapabilities.FIREFOX
        caps["marionette"] = True
        caps["binary"] = self.firefox_path

        self.driver = webdriver.Firefox(capabilities=caps)
        self.driver.get(resource)
        
    def set_iterations(self,new_interation):
        self.iterations =  new_iteration

    def find_elem(self, string):
        return self.driver.find_element_by_id(string)
    
    def refresh_browser(self):
        self.driver.refresh()

    def process(self,fcn):
        for i in range(0,self.iterations):
            fcn()
