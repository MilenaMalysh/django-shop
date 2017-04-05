import os
import random
import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from shop.tests.login import Login


class BasketTest(Login):
    def test_product_from_basket_button_disabled(self):
        driver = self.driver
        driver.get(os.environ['URL']+'basket')

        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, "basket-list"))
        )

        products = driver.find_elements_by_css_selector("ul.basket-list li")
        if len(products) == 0:
            self.assertTrue(True)
        else:
            index = random.randint(0, len(products) - 1)
            product = products[index].find_element_by_tag_name('h3').text
            driver.find_element_by_class_name("logo-pic").click()
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.CLASS_NAME, "products-list"))
            )
            for i in driver.find_elements_by_css_selector("ul.products-list li"):
                if product == (i.text).split("\n")[0]:
                    i.find_element_by_tag_name("img").click()
                    break

            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.CLASS_NAME, "card__article"))
            )

            self.assertTrue('disabled' in driver.find_element_by_id("to_basket").get_attribute("class"))

    def test_add_product_to_basket(self):
        driver = self.driver
        driver.get(os.environ['URL'])
        products = driver.find_elements_by_css_selector("ul.products-list img")
        if len(products) == 0:
            self.assertTrue(True)
        else:
            for i in range(len(products)):
                WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "products-list"))
                )
                products = driver.find_elements_by_css_selector("ul.products-list img")
                products[i].click()
                WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "card__article"))
                )
                if 'disabled' in driver.find_element_by_id("to_basket").get_attribute("class"):
                    driver.get(os.environ['URL'])
                else:
                    product = driver.find_element_by_class_name("product-name").text
                    driver.find_element_by_id("to_basket").click()
                    break
            driver.get(os.environ['URL'] + 'basket')

            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.CLASS_NAME, "basket-list"))
            )

            self.assertTrue(product in driver.page_source)


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(BasketTest('test_product_from_basket_button_disabled'))
    test_suite.addTest(BasketTest('test_add_product_to_basket'))
    return test_suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(failfast=True)
    runner.run(suite())