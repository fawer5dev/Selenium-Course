# Import the necessary modules from Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import time

# Create a Edge browser instance
# driver = webdriver.Chrome()
driver = webdriver.Edge()

# Maximize the window
driver.maximize_window()
t=2
# Wait for x seconds
time.sleep(t)
driver.implicitly_wait(15)

# Navigate to the 'Text Box' page on DemoQA
driver.get('https://demoqa.com/select-menu')

# Find the element with the 'userName' attribute XPath and enter the text xxx into it
group = driver.find_element(By.XPATH, "//DIV[@class='css-1hwfws3'][3]")

"""element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//DIV[@class=' css-1hwfws3'][1]")))"""
ds = Select(group)
ds.select_by_visible_text("Group 2, option 1")
ds.select_by_index(3)
time.sleep(t)
driver.close()


