from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")


driver.get("https://phptravels.org/register.php")
driver.maximize_window()
driver.find_element(By.ID, 'inputFirstName').send_keys("Ramadevi")
driver.find_element(By.ID, 'inputLastName').send_keys("ch")
driver.find_element(By.ID, 'inputEmail').send_keys("rongala.ramadevi@gmail.com")
driver.find_element(By.ID, 'inputPhone').send_keys("9086868666687")


driver.find_element(By.CSS_SELECTOR, '#inputCompanyName').send_keys("xyz")
driver.find_element(By.XPATH, "//input[@id='inputAddress1']").send_keys("kphb phase-1")

driver.find_element(By.ID, 'inputAddress2').send_keys("Gokulplots")
driver.find_element(By.ID, 'inputCity').send_keys("HYD")
driver.find_element(By.ID, 'stateinput').send_keys("Telangana")
driver.find_element(By.ID, 'inputPostcode').send_keys("5000085")

drop_down = Select(driver.find_element(By.XPATH, "//select[@id='inputCountry']"))
drop_down.select_by_visible_text("India")
import time
time.sleep(5)

driver.find_element(By.XPATH, "//input[@id='customfield2']").send_keys("909898980989809")
driver.find_element(By.CSS_SELECTOR, "#inputNewPassword1").send_keys("Rama12771277")
driver.find_element(By.CSS_SELECTOR, "#inputNewPassword2").send_keys("Rama12771277")

#driver.find_element(By.XPATH, "//button[normalize-space()='Generate Password']").click()

driver.find_element(By.XPATH, "//div[@id='#divDynamicRecaptcha1']").click()
time.sleep(2)
driver.find_element(By.XPATH, '//body[1]/section[1]/div[1]/div[1]/div[2]/div[1]/form[1]/p[1]/input[1]').click()
time.sleep(5)

driver.close()


