from selenium.webdriver.common.by import By

class Sigh_Up_Page:
    X_BUTTON =(By.XPATH, '//button[text()=\'Sign up\']')
    INPUT_NAME = (By.XPATH, '//input[@id=\'signupName\']')
    INPUT_LAST_NAME = (By.XPATH, '//input[@id=\'signupLastName\']')
    INPUT_EMAIL = (By.XPATH, '//input[@name=\"email\"]')
    INPUT_PASSWORD = (By.XPATH, '//input[@name="password" and @type="password"]')
    RE_ENTER_PASSWORD = (By.XPATH, '//input[@name="repeatPassword" and @type="password"]')
    REGISTER = (By.XPATH, '//button[@type=\'button\' and text()=\'Register\']')

    def __init__(self, driver):
        self.driver = driver



    def name_field(self):
        return self.driver.find_element(self.INPUT_NAME[0], self.INPUT_NAME[1])

    def last_name_field(self):
        return self.driver.find_element(self.INPUT_LAST_NAME[0], self.INPUT_LAST_NAME[1])

    def email_field(self):
        return self.driver.find_element(self.INPUT_EMAIL[0], self.INPUT_EMAIL[1])

    def password_field(self):
        return self.driver.find_element(self.INPUT_PASSWORD[0], self.INPUT_PASSWORD[1])

    def reenter_password_field(self):
        return self.driver.find_element(self.RE_ENTER_PASSWORD[0], self.RE_ENTER_PASSWORD[1])

    def register_button(self):
        return self.driver.find_element(self.REGISTER[0], self.REGISTER[1])

    def x_button(self):
        return self.driver.find_element(self.X_BUTTON[0], self.X_BUTTON[1])