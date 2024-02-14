from selenium import webdriver

import time

from sample_project.pages.LoginPage import LoginPage
from sample_project.pages.HomePage import HomePage

from selenium.webdriver.common.by import By

import

import unittest

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_test(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        login = LoginPage(driver)
        login.enter_username('Admin')
        login.enter_password('admin123')
        login.click_login()
        #Class for the HomePage
        homepage = HomePage(driver)
        homepage.click_welcom()
        homepage.click_logout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("TestCompleted")


if __name__ == '__main__':
    unittest.main()






