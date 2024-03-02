from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

#driver = webdriver.Chrome(ChromeDriverManager().install())
my_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"


from seleniumbase import SB

global exit_flag
exit_flag = False

with SB(uc=True) as sb:
     #sb.driver.uc_open_with_reconnect(
     #   "https://www.usvisascheduling.com/en-US/",
       #  reconnect_time=1200
     #)
     sb.open("https://www.usvisascheduling.com/en-US/")
     time.sleep(2)
     sb.type("#signInName", "SHIRAJ FATWANI")
     sb.type("#password", "Fatwani@1983")
     # captcha_element = sb.wait_for_element_visible("#captchaImage")
     # time.sleep(1)  # Adjust the wait time as needed
     # captcha_image_base64 = sb.driver.execute_script("""
     #                  var img = document.querySelector("#captchaImage");
     #                  var canvas = document.createElement('canvas');
     #                  canvas.width = img.width;
     #                  canvas.height = img.height;
     #                  var ctx = canvas.getContext('2d');
     #                  ctx.drawImage(img, 0, 0);
     #                  return canvas.toDataURL();""")
     #
     # time.sleep(5)
     # print(captcha_image_base64.split(","))
     # import base64
     # print(base64.b64decode(captcha_image_base64.split(",")[1]))
     # import pybase64
     # from PIL import Image
     # from io import BytesIO
     # import pytesseract
     # image_data = pybase64.b64decode(captcha_image_base64.split(",")[1])
     # captcha_image = Image.open(BytesIO(image_data))
     # time.sleep(1)
     # print(captcha_image)
     # pytesseract.pytesseract.tesseract_cmd = 'C:/Users/rcheepurupalli/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'
     # captcha_text = pytesseract.image_to_string(captcha_image)
     # print("captcha" + captcha_text)
     # # Enter the extracted text into the CAPTCHA input field
     # #captcha_input = sb.find_element("#extension_atlasCaptchaResponse")
     # #captcha_input.send_keys(captcha_text)
     time.sleep(10)

     sb.click("#continue")
     time.sleep(5)
     ####entering security fields
     if sb.is_element_present("#kbq1ReadOnly") or sb.is_element_present("#kbq1aReadOnly") or sb.is_element_present("#kbq1bReadOnly"):
          sb.type("#kba1_response", "MUMBAI")
     if sb.is_element_present("#kbq2aReadOnly") or sb.is_element_present("#kbq2bReadOnly") or sb.is_element_present("#kbq2ReadOnly"):
          sb.type("#kba2_response", "PIZZA")
     if sb.is_element_present('#kbq3ReadOnly') or sb.is_element_present("#kbq3aReadOnly") or sb.is_element_present("#kbq3bReadOnly"):
          sb.type("#kba3_response", "MIRA ROAD")
     sb.click("#continue")
     time.sleep(5)
     sb.click("#continue_application")
     time.sleep(30)
     import pdb;pdb.set_trace()
     list_of_options = sb.get_select_options("#post_select", attribute="text")
     print(list_of_options)
     input_filed = []
     for each_item in list_of_options[1:]:
          if exit_flag:
               print("selected slot.......")
               break
          else:
               sb.click("#post_select")
               sb.select_option_by_text("#post_select", each_item)
               sb.wait_for_element_visible("#datepicker")
               sb.click("#datepicker")
          for each in range(24):
               if sb.find_visible_elements(".greenday"):
                    input_filed = sb.find_visible_elements(".greenday")
                    sb.click(".greenday")
                    sb.click("div.col-sm-6 label input")
                    exit_flag = True
                    break
               else:
                    time.sleep(5)
                    sb.click(".ui-icon.ui-icon-circle-triangle-e")





#options = webdriver.ChromeOptions()

#options.add_argument("start-maximized")
#options.add_experimental_option("excludeSwitches", ["enable-automation"])
#options.add_experimental_option('useAutomationExtension', False)
#driver = webdriver.Chrome(options=options, executable_path="C:\Drivers\chromedriver-win32\chromedriver.exe")


#options.add_argument("start-maximized")
#options.add_argument(f"user-agent={my_user_agent}")
#driver = uc.Chrome(options=options)


#driver.maximize_window()
time.sleep(3)

# sb.driver.find_element(By.ID, "signInName").send_keys("SHIRAJ FATWANI")
# sb.driver.find_element(By.ID, "password").send_keys("Fatwani@1983")
# time.sleep(10)
# sb.driver.find_element(By.ID, "continue").click()
# time.sleep(20)
#
#
# driver.find_element(By.ID, 'continue_application').click()
# wait = WebDriverWait(driver, 10)
# time.sleep(10)
#
# elemt = wait.until(EC.presence_of_element_located((By.ID, 'post_select')))
#
# selext_obj = Select(elemt)
#
# print(len(selext_obj.options))

time.sleep(30)

