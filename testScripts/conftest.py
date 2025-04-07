import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import tempfile
import uuid

@pytest.fixture(scope="function")
def setup(browser):
    """
    Fixture to initialize and return the appropriate WebDriver instance based on the browser choice.
    Creates a unique --user-data-dir to avoid session conflicts in parallel test runs.
    """

    if browser == 'chrome':
        chrome_options = ChromeOptions()
        chrome_options.add_argument("start-maximized")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

        # Create a unique user data dir for parallel sessions
        user_data_dir = tempfile.mkdtemp(suffix=str(uuid.uuid4()))
        chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    elif browser == 'firefox':
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--width=1920")
        firefox_options.add_argument("--height=1080")

        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    yield driver
    driver.quit()

def pytest_addoption(parser):
    """
    Adds a command-line option to specify the browser: --browser=chrome or --browser=firefox
    """
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests against")

@pytest.fixture()
def browser(request):
    """
    Reads the --browser value provided via CLI and passes it to fixtures.
    """
    return request.config.getoption("--browser")








# from selenium import webdriver
# import pytest
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from webdriver_manager.chrome import ChromeDriverManager
# # import chromedriver_autoinstaller as chromedriver
# from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.chrome.options import Options

# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# chrome_options = Options()

# options = webdriver.ChromeOptions()
# options.add_argument("start-maximized")
# options.add_argument("--disable-extensions")
# # options.add_argument("--disable-infobars")
# # options.add_argument("--disable-notifications")
# # options.add_argument("--disable-popup-blocking")
# # options.add_argument("--disable-gpu")
# options.add_argument("--disable-dev-shm-usage")
# # options.add_argument("headless")
# options.add_argument("--disable-dev-shm-usage")
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# # options.add_experimental_option("prefs", {
# #     "profile.default_content_setting_values.notifications": 2
# # })

# @pytest.fixture()
# def setup(browser):
#     global driver
#     if browser == 'chrome':
#         driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
#     elif browser == 'firefox':
#         driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
#     return driver


# def pytest_addoption(parser):    # This will get the value from CLI/hooks
#     parser.addoption("--browser")

# @pytest.fixture()
# def browser(request):    # This will return the Browser value to the setup method.
#     return request.config.getoption("--browser")
