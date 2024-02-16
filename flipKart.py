import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

option = Options()
option.add_argument('--disable-notifications')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)

driver.get("https://www.flipkart.com/")

driver.implicitly_wait(2)


search_field = driver.find_element(By.XPATH, "//input[@class='Pke_EE']")
search_field.send_keys("mobile")
#import pdb;pdb.set_trace()
search_field.send_keys(Keys.ENTER)

img = driver.find_element(By.XPATH, "//div[@data-id='MOBGTAGPAQNVFZZY']//div[@class='col col-5-12 nlI3QM']//img")
with open('Logo.png', 'wb') as file:
   img = driver.find_element(By.XPATH, "//div[@data-id='MOBGTAGPAQNVFZZY']//div[@class='col col-5-12 nlI3QM']//img")
   file.write(img.screenshot_as_png)
time.sleep(10)
print(img.get_attribute('src'))





driver.close()

