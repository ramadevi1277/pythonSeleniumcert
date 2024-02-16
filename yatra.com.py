from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

option = Options()
# Working with the 'add_argument' Method to modify Driver Default Notification
option.add_argument('--disable-notifications')

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option)

driver.maximize_window()
time.sleep(5)
driver.get("https://www.yatra.com/")

driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, "#BE_flight_origin_city").click()



input=driver.find_elements(By.XPATH, "//li//div[@class='ac_airport']//p[@class='ac_cityname']")

time.sleep(5)

for each in input:
    if each.text == "Chennai (MAA)":
        print(each.text)
        time.sleep(5)
        input_entry = each
        break


input_entry.click()

time.sleep(10)


print(len(input))


driver.quit()
