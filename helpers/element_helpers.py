from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def find_element(driver, xpath):
    element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    element.click()


def find_elements(driver, xpath):
    elements = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, xpath)))
    return elements


def find_but_not_click(driver, xpath):
    element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    return element


def find_elements_but_not_click(driver, xpath):
    element = WebDriverWait(driver, 10).until(EC.visibility_of_any_elements_located((By.XPATH, xpath)))
    return element
