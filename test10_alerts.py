# Import the necessary modules from Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Create a Edge browser instance
# driver = webdriver.Chrome()
driver = webdriver.Edge()

# Wait for x seconds
t=2
time.sleep(t)

# Navigate to the 'Text Box' page on DemoQA
driver.get('https://testingqarvn.com.es/colegio/')

# Maximize the window
driver.maximize_window()

# Find the SELECT MENU with the attribute CLASS_NAME and Select it.
driver.find_element(By.XPATH, "//input[@id='itsanimage']").click()