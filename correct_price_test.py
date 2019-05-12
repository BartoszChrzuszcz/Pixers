import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from variables import chromedriver_path as chrome_path, paths_to_elements as path
from helpers import element_helpers as eh


class ProductPriceTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path=chrome_path.ChromedriverPath.CHROMEDRIVER_PATH)
        self.base_url = 'https://pixers.pl/'

    def test_price_from_list(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        category_element = eh.find_but_not_click(driver, path.PAINTS_AND_POSTER)
        actions = ActionChains(driver)
        actions.move_to_element(category_element).perform()
        eh.find_element(driver, path.PAINTS_ON_PLEXI)
        eh.find_element(driver, path.POPUP)
        list_price = eh.find_but_not_click(driver, path.PRICE_FROM_LIST)
        list_price_text = list_price.text
        eh.find_element(driver, path.FIRST_ELEMENT)
        item_card_price = eh.find_but_not_click(driver, path.PRODUCT_CARD_PRICE)
        item_card_price_text = item_card_price.text
        self.assertEqual(list_price_text, item_card_price_text,
                         f'price from list do not match price from item card: {list_price_text}')

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
