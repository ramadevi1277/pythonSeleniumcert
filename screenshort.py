from selenium import webdriver
from selenium.webdriver.chrome.service import Service



driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()
driver.get("http://newtours.demoaut.com/mercurywelcome.php")

driver.save_screenshot("C:\Screenshorts\image.png")

driver.close()