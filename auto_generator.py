from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from element_manager import *
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(ChromeDriverManager().install())
# to open the url in browser
driver.get('https://www.google.com/')

# to open the url in browser
driver.get('https://www.google.com/')

# to type content in input field
driver.find_element(By.XPATH,get_xpath(driver,'Y8Gm5QmVpnb5bg6')).send_keys('fli')

# press ArrowDown key
driver.switch_to.active_element.send_keys(Keys.ARROW_DOWN)

# press Enter key
driver.switch_to.active_element.send_keys(Keys.ENTER)

# to fetch the text of element
text=driver.find_element(By.XPATH, get_xpath(driver,'9sWuHFdhgeQ0jQh')).text

