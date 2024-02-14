from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

#from webdriver_manager.firefox import GeckoDriverManager

#from webdriver_manager.microsoft import IEDriverManager

import time

driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#driver = webdriver.Ie(IEDriverManager().install())

driver.maximize_window()


time.sleep(5)
driver.get("http://youtube.com/")
input = driver.find_element(By.XPATH, "//input[@id='search']")
input.send_keys("hi this is a test")
input.send_keys(Keys.CONTROL+"a")
input.send_keys(Keys.CONTROL+"x")
time.sleep(5)
actions = ActionChains(driver)
actions.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()


time.sleep(10)

print(driver.title)
driver.close()