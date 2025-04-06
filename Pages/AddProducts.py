from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class AddProductPage:

    def __init__(self, driver):
        self.driver = driver

    def addBackpack(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='inventory_list']//div[1]//div[3]//button[1]"))).click()

    def shoppingContainer(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='shopping_cart_container']"))).click()

    def removeProduct(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='REMOVE']"))).click()