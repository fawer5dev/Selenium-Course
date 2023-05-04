# Import the necessary modules from Selenium
import unittest
from selenium import webdriver
from Funciones.Funciones import Funciones_Globales

# Wait for x seconds
tg = .2


class base_test(unittest.TestCase):
    def setUp(self):
        # Create a Edge browser instance
        self.driver = webdriver.Edge()
        # Maximize the window
        self.driver.maximize_window()

    # Define a test function
    def test1(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar("https://www.saucedemo.com/", 1)
        # f.Texto_Xpath("//INPUT[@id='user-name']", "Fawer", .3)
        # f.Texto_Xpath("//INPUT[@id='password']", "abc123", .3)
        # f.Texto_ID("user-name", "Fawer", .3)
        # f.Texto_ID("password", "abc123", .3)
        # f.Texto_Xpath_Valida("//INPUT[@id='user-name']", "Fawer", t)
        # f.Texto_Xpath_Valida("//INPUT[@id='password']", "abc123", t)
        f.Texto_Mixto("id", "userName", "Fawer", tg)
        f.Texto_Mixto("id", "userEmail", "xxx@gmail.com", tg)
        f.Texto_Mixto("id", "currentAddress", "Demo uno de texto, para pruebas.", tg)
        f.Texto_Mixto("id", "permanentAddress", "Demo uno de texto, para pruebas.", tg)
        f.Click_Mixto("id", "submit", tg)

    def tearDown(self):
        driver = self.driver
        driver.close()


# If this script is run directly, run all the defined tests
if __name__ == "__main__":
    unittest.main()