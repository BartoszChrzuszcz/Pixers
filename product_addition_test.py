import time
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from variables import chromedriver_path as chrome_path, paths_to_elements as path, fixed_values as fv
from helpers import element_helpers as eh


class ProductAdditionTests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path=chrome_path.ChromedriverPath.CHROMEDRIVER_PATH)
        self.base_url = 'https://pixers.pl/'

    def test_one_product_added_to_basket(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        category_element = eh.find_but_not_click(driver, path.PAINTS_AND_POSTER)
        actions = ActionChains(driver)
        actions.move_to_element(category_element).perform()
        eh.find_element(driver, path.PAINTS_ON_PLEXI)
        eh.find_element(driver, path.POPUP)
        eh.find_element(driver, path.FIRST_ELEMENT)
        eh.find_element(driver, path.CONFIGURATION)
        eh.find_element(driver, path.DROPDOWN)
        eh.find_element(driver, path.DESIRED_SIZE)
        price_after_configuration = eh.find_but_not_click(driver, path.PRICE_AFTER_CONFIGURATION)
        print(price_after_configuration.text)
        time.sleep(0.5)
        eh.find_element(driver, path.BUY_NOW_BUTTON)
        eh.find_element(driver, path.SUBMIT)
        price_in_cart = eh.find_but_not_click(driver, path.PRODUCT_IN_CART_PRICE)
        price_in_cart_text = price_in_cart.text
        quntity = eh.find_but_not_click(driver, path.ITEMS_IN_CART)
        self.assertEqual(fv.ITEM_QUANTITY, quntity.text,
                         f'there is more than one item in cart: {fv.ITEM_QUANTITY}')
        assert '287' in price_in_cart_text


    @classmethod
    def tearDownClass(self):
        self.driver.quit()
