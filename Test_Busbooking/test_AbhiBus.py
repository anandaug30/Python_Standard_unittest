import unittest
from selenium import webdriver
from PageObject import Home_Page as pom
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='..//Drivers/chromedriver.exe')
driver.get("https://www.abhibus.com/")
assert "Online Bus Ticket Booking" in driver.title
print(pom.WelcomeScreen.FilterBusOptions.txt_source['id'])

elem = driver.find_element_by_id(pom.WelcomeScreen.FilterBusOptions.txt_source['id'])
elem.send_keys('Hyderabad')

driver.close()
driver.quit()