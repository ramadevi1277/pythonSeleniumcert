from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()
time.sleep(5)
driver.get("https://www.yatra.com/")

driver.implicitly_wait(5)

driver.find_element(By.CSS_SELECTOR, "#BE_flight_origsin_city").click()


input = driver.find_elements(By.XPATH, "//div[@class='ac_results origin_ac']//li//p[@class='ac_airportname']")
input = driver.find_elements(By.XPATH, "//div[@class='ac_results origin_ac']//ul")


for each in input:
    import pdb;pdb.set_trace()
    if each.text() == "Indira Gandhi International":
        each.click()


print(len(input))


driver.quit()
