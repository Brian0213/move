import time
import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../pageObjects')))
from Pages.LoginPage import LoginPage
from utility.readProperties import ReadConfig
from utility.customLogger import LogGen

class Test_001_Login:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.order(1)
    def test_login(self, setup):
        self.logger.info("******** Verifying Login test ********")
        self.logger.info("********Call the Browser Configuration********")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURL)
        self.logger.info("********Define the LoginPage Driver********")
        self.lp = LoginPage(self.driver)
        time.sleep(5)
        self.logger.info("********Type the Username*******")
        self.lp.setUserName(self.username)
        time.sleep(3)
        self.logger.info("********Type the Password*******")
        self.lp.setPassword(self.password)
        time.sleep(3)
        self.logger.info("******** Click the Log in Button*******")
        self.lp.clickLogin()
        time.sleep(3)
        self.logger.info("******** Click the Logout Menu*******")
        self.lp.logoutMenu()
        time.sleep(3)
        self.logger.info("******** Click the Logout Link*******")
        self.lp.logoutLink()
        time.sleep(8)
        self.logger.info("********Login Test is successful********")
        self.driver.quit()