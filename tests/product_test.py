import os
import random
import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from shop.tests.login import Login
from shop.tests.utils import check_exists_by_class


class ProductTest(Login):
    def test_open_product(self):
        driver = self.driver
        driver.get(os.environ['URL'])
        products = driver.find_elements_by_css_selector("ul.products-list li")
        index = random.randint(0, len(products)-1)
        products[index].find_element_by_tag_name('img').click()
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, "card__article"))
        )
        self.assertTrue(check_exists_by_class(driver, 'card__article'))

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(ProductTest('test_open_product'))
    return test_suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(failfast=True)
    runner.run(suite())