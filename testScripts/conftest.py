from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
# import chromedriver_autoinstaller as chromedriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

chrome_options = Options()

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("--disable-extensions")
options.add_argument("--disable-infobars")
options.add_argument("--disable-notifications")
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage")
# options.add_argument("headless")
options.add_argument("--disable-dev-shm-usage")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2
})

@pytest.fixture()
def setup(browser):
    global driver
    if browser == 'chrome':
        driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    elif browser == 'firefox':
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    return driver


def pytest_addoption(parser):    # This will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):    # This will return the Browser value to the setup method.
    return request.config.getoption("--browser")
