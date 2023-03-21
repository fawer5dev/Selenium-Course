# Import the necessary modules from Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time

# Create a Edge browser instance
driver = webdriver.Edge()

# Maximize the window
driver.maximize_window()
t=2
# Wait for x seconds
time.sleep(t)
driver.implicitly_wait(15)

# Navigate to the 'Text Box' page on DemoQA
driver.get('https://demoqa.com/select-menu')

# Find the SELECT MENU with the attribute CLASS_NAME and Select it.
try:
    driver.find_element(By.CLASS_NAME, "css-2b097c-container").click();
    time.sleep(t)
    driver.quit()
except TimeoutException as ex:
    print(ex.msg + "EROOR TIMEOUT ")
    driver.close()