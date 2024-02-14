class HomePage():

    def __init__(self, driver):
        self.deriver = driver

        self.welcome_link_id = 'welcome'
        self.logout_link_text = 'Logout'

    def click_welcom(self):
        self.driver.find_element(By.ID, self.welcome_link_id).click()

    def click_logout(self):
        self.driver.find_element(By.ID, self.logout_link_text).click()



