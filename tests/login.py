import os
import unittest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        driver = self.driver
        url = os.environ['URL']
        driver.get(url)
        passw = driver.find_element_by_name("password")
        passw.send_keys(os.environ['PASSWORD'])
        login = driver.find_element_by_name("username")
        login.send_keys(os.environ['LOGIN'])
        driver.find_element_by_class_name("login-btn").click()
        WebDriverWait(self.driver, 30).until(EC.staleness_of(login))

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()