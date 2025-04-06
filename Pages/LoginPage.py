from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        WebDriverWait(self.driver, 10).until( EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']"))).clear()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']"))).send_keys(username)

    def setContinue(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Continue')]"))).click()

    def setPassword(self, password):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']"))).clear()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']"))).send_keys(password)

    def clickLogin(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='login-button']"))).click()
        # self.driver.find_element(By.CLASS_NAME, "self.button_class_name").click()

    def logoutMenu(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='bm-burger-button'] button"))).click()

    def logoutLink(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='logout_sidebar_link']"))).click()