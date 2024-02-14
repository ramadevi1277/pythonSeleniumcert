from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

# driver.maximize_window()
# driver.get("https://gmail.com/")
# time.sleep(60)
# driver.find_element(By.ID, 'identifierId').send_keys("rongala.ramadevi@gmail.com")
# #driver.find_element(By.XPATH, "//span[contains(text(),'Next')]").click()
# driver.find_element(By.XPATH, "//span[text()='Next']").click()
# time.sleep(1)
# driver.save_screenshot("C:\Screenshorts\image2.png")
# driver.find_element(By.NAME, 'password' ).send_keys("Rama@1277")
# driver.find_element(By.TAG_NAME, 'span').click()
# driver.quit()

import pytest
from selenium.webdriver.common.by import By
from conftest import *
#from tests.test_login import Test_login
import time
from selenium_helper import Selenium_Helper
from pages.homepage import HomePage
from selenium.webdriver.common.by import By
from pages.loginpage import LoginPage
from datetime import datetime


#locators
configuration_tab  = (By.XPATH, "//a[@class='nav-link']")
text_on_configuration_tab = (By.XPATH, "//span[@class='app-titles']")

@pytest.mark.usefixtures("browser_setup")
class CheckConfigurationTab():
    expected_title = "AdaptiveMobile Security"
    helper = Selenium_Helper(driver)

    def _validate_page(self, driver):
        '''Validate login to pxp.'''
        if driver.title != "AdaptiveMobile Securitykkk":
            raise InvalidPageError("This is not PMC Page. Currently at %s" %(driver.current_url))

