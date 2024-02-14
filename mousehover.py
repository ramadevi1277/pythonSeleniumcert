from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com")
time.sleep(5)

driver.find_element(By.ID, 'txtUsername').send_keys("Admin")
driver.find_element(By.XPATH, "//input[@name='txtPassword']").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR, ".button").click()
driver.get_screenshot_as_png()
text=driver.find_element(By.CSS_SELECTOR, '#spanMessage').text()
driver.close()
