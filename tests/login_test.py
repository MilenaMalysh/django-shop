import os
import unittest

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from shop.tests.utils import string_generator, check_exists_by_class


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_login_success(self):
        driver = self.driver
        driver.get(os.environ['URL'])
        passw = driver.find_element_by_name("password")
        passw.send_keys(os.environ['PASSWORD'])
        login = driver.find_element_by_name("username")
        login.send_keys(os.environ['LOGIN'])
        driver.find_element_by_class_name("login-btn").click()
        WebDriverWait(self.driver, 30).until(EC.staleness_of(login))
        self.assertFalse(check_exists_by_class(driver, "login-btn"))

    def test_login_failure(self):
        driver = self.driver
        driver.get(os.environ['URL'])
        passw = driver.find_element_by_name("password")
        passw.send_keys(string_generator())
        login = driver.find_element_by_name("username")
        login.send_keys(string_generator())
        driver.find_element_by_class_name("login-btn").click()
        WebDriverWait(self.driver, 30).until(EC.staleness_of(login))
        self.assertTrue(check_exists_by_class(driver, "login-btn"))

    def tearDown(self):
        self.driver.close()


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(LoginTest('test_login_success'))
    test_suite.addTest(LoginTest('test_login_failure'))
    return test_suite

if __name__ == "__main__":
    unittest.main()