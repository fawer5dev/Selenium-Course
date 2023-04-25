# Import the necessary modules from Selenium
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Wait for x seconds
t=2

class base_test(unittest.TestCase):
    def setUp(self):
        # Create a Edge browser instance
        self.driver = webdriver.Edge()
        # Maximize the window
        self.driver.maximize_window()
        time.sleep(t)

    # Define a test function
    def test1(self):
        driver = self.driver
        driver.get('https://demoqa.com/')
        time.sleep(t)

    def tearDown(self):
        driver = self.driver
        driver.close()

# If this script is run directly, run all the defined tests
if __name__ == "__main__":
    unittest.main()