ecimport os
from selenium import webdriver

chromedriver = "~/Documents/chromedriver/wires"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://google.com")
driver.quit()
    
