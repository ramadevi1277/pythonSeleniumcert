# Import necessary modules
import time
# from PIL import Image
# import pytesseract
from seleniumbase import SB
# import base64
# from io import BytesIO
import argparse

# Global variable
global exit_flag
exit_flag = False

# Create a parser object
parser = argparse.ArgumentParser(description='Script to automate web tasks.')

# Add command-line options
parser.add_argument('-m', '--month', type=int, default=16, help='Number of Months to select (1-100).')
parser.add_argument('-c', '--choices', type=str,
                    default="CHENNAI VAC,HYDERABAD VAC,KOLKATA VAC,MUMBAI VAC,NEW DELHI VAC",
                    help='List of choices, use comma separated')
parser.add_argument('-s', '--slotcount', type=int, default=5, help='slot count')

# Parse the command-line arguments
args = parser.parse_args()

# Access the value of the month option
selected_month = args.month
slotcount = args.slotcount

# Split the choices string and store it in a list
choices = [""] + args.choices.split(',') if args.choices else [args.choices]

from selenium.common.exceptions import NoSuchElementException

# Initialize SeleniumBase instance
with SB(uc=True, headless=False) as sb:
    sb.driver.uc_open_with_reconnect(
        "https://www.usvisascheduling.com/en-US/",
        reconnect_time=2
    )

    # Login
    sb.wait_for_element_visible("#signInName", timeout=30)
    sb.type("#signInName", "")
    sb.type("#password", "s")
    #time.sleep(60)
    #expected_title = "Visa Application Home · Customer Self-Service"
    #sb.assert_title(expected_title)
    sb.wait_for_element_visible("#continue_application", timeout=120)
    sb.click("#continue_application")

    # Wait for elements
    sb.wait_for_element_visible("#post_select", timeout=30)
    list_of_options = sb.get_select_options("#post_select", attribute="text")
    print(list_of_options)
    print(choices)
    sb.wait_for_element_visible("#gm_select", timeout=120)
    #time.sleep(5)

    # Loop through choices
    while True:
        try:
            for each_item in choices[1:]:
                if each_item in list_of_options:
                    if not exit_flag:
                        sb.click("#post_select")
                        sb.select_option_by_text("#post_select", list_of_options[0])
                    if exit_flag:
                        print("selected slot.......")
                        time.sleep(300)
                        break
                    else:
                        sb.click("#post_select")
                        sb.select_option_by_text("#post_select", each_item)
                        sb.is_element_clickable("#datepicker")
                        sb.wait_for_element_visible("#datepicker", timeout=100)
                        datepicker = sb.find_element(".form-control.hasDatepicker")
                        datepicker.click()

                        # Loop through months
                        for each in range(selected_month):
                            if sb.find_visible_elements(".greenday"):
                                input_filed = sb.find_visible_elements(".greenday")
                                sb.click(".greenday")
                                list_of_availablity_slots = sb.find_elements('.col-sm-6 label input')
                                if list_of_availablity_slots == []:
                                    list_of_availablity_slots = sb.find_element('.col-sm-6 label input')
                                    if list_of_availablity_slots:
                                        print("only one slot is available selecting next date....")
                                        sb.is_element_clickable("#datepicker")
                                        sb.wait_for_element_visible("#datepicker", timeout=100)
                                        datepicker.click()
                                    else:
                                        print("Not found slots selecting next date......")
                                else:
                                    print("Radio button count:", len(list_of_availablity_slots))
                                    if len(list_of_availablity_slots) > 1:
                                        for each_text in range(1, (len(list_of_availablity_slots) + 1)):
                                            if int(sb.get_text("div.col-sm-6:nth-of-type(%d) label" % (each_text))[
                                                   7:-1]) >= slotcount:
                                                sb.click_xpath(
                                                    "//div[%d][@class='col-sm-6']//label//input" % (each_text))
                                                exit_flag = True
                                                break
                                            else:
                                                sb.click_xpath(
                                                    "//div[%d][@class='col-sm-6']//label//input" % (each_text))
                                                print("selected slot...")
                                                time.sleep(6000)
                                                exit_flag = True
                                                break
                                    else:
                                        print("no slots found %d" % len(list_of_availablity_slots))
                            else:
                                sb.wait_for_element_visible(".ui-icon.ui-icon-circle-triangle-e", timeout=120)
                                sb.click(".ui-icon.ui-icon-circle-triangle-e")
        except NoSuchElementException as e:
            print(f"No such element found: {e}")
            continue