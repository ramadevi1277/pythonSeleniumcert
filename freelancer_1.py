import time
from PIL import Image
import pytesseract
from seleniumbase import SB
import base64
from io import BytesIO

global exit_flag
exit_flag = False
with SB(uc=True) as sb:
    # sb.driver.uc_open_with_reconnect(
    #   "https://www.usvisascheduling.com/en-US/",
    #  reconnect_time=1200
    # )
    sb.open("https://www.usvisascheduling.com/en-US/")
    sb.wait_for_element_visible("#signInName", timeout=30)
    sb.type("#signInName", "Vivekr_1980")
    sb.type("#password", "Vivek@1980")
    time.sleep(10)
    sb.click("#continue")
    sb.wait_for_element_visible("#kba1_response", timeout=70)
    #Entering security questions
    if sb.is_element_present("#kbq1ReadOnly") or sb.is_element_present("#kbq1aReadOnly") or sb.is_element_present(
            "#kbq1bReadOnly"):
        sb.type("#kba1_response", "shartha")
    if sb.is_element_present("#kbq2aReadOnly") or sb.is_element_present("#kbq2bReadOnly") or sb.is_element_present(
            "#kbq2ReadOnly"):
        sb.type("#kba2_response", "gandhinagar")
    if sb.is_element_present('#kbq3ReadOnly') or sb.is_element_present("#kbq3aReadOnly") or sb.is_element_present(
            "#kbq3bReadOnly"):
        sb.type("#kba3_response", "sertha")
    sb.click("#continue")
    sb.wait_for_element_visible("#continue_application", timeout=30)
    sb.click("#continue_application")
    sb.wait_for_element_visible('.list-group-item.py-0', timeout=70)
    sb.wait_for_element_visible("#post_select", timeout=30)
    list_of_options = sb.get_select_options("#post_select", attribute="text")
    print(list_of_options)
    input_filed = []
    for each_item in list_of_options[1:]:
        if exit_flag == False:
            sb.click("#post_select")
            sb.select_option_by_text("#post_select", list_of_options[0])
        if exit_flag:
            print("selected slot.......")
            time.sleep(300)
            break
        else:
            sb.click("#post_select")
            sb.select_option_by_text("#post_select", each_item)
            # time.sleep(5)
            sb.wait_for_element_visible("#datepicker", timeout=10)
            sb.click("#datepicker")
        for each in range(24):
            if exit_flag:
                break
            if sb.find_visible_elements(".greenday"):
                input_filed = sb.find_visible_elements(".greenday")
                sb.click(".greenday")
                list_of_availablity_slots = sb.find_visible_elements('.col-sm-6')
                if len(list_of_availablity_slots) > 1:
                    for each_text in range(1, (len(list_of_availablity_slots)+1)):
                        if int(sb.get_text("div.col-sm-6:nth-of-type(%d) label" % (each_text))[7:-1]) >= 4:
                            #import pdb;pdb.set_trace()
                            sb.click_xpath("//div[%d][@class='col-sm-6']//label//input" % (each_text))
                            exit_flag = True
                            break
                else:
                    sb.click("div.col-sm-6 label input")
                    exit_flag = True

            else:
                # time.sleep(5)
                sb.wait_for_element_visible(".ui-icon.ui-icon-circle-triangle-e", timeout=120)
                sb.click(".ui-icon.ui-icon-circle-triangle-e")