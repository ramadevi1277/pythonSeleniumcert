from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time
####to copy and past the text again
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("http://youtube.com/")
input = driver.find_element(By.XPATH, "//input[@id='search']")
input.send_keys("hi this is a test")
input.send_keys(Keys.CONTROL+"a")
input.send_keys(Keys.CONTROL+"x")
time.sleep(5)
actions = ActionChains(driver)
actions.key_down(Keys.CONTROL).send_keys("t").key_up(Keys.CONTROL).perform()


### to open new tab
window_before = driver.window_handles[0]

link="https://www.google.com"
driver.execute_script("window.open('{}');".format(link))
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)

#driver.find_element_by_name("q").send_keys("test")

#script = "alert('Alert via selenium')"

# generate a alert via javascript
#driver.execute_script(script)
#driver.switchTo().alert().accept();
time.sleep(5)

