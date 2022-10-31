from selenium.webdriver.common.by import By

from curs12_tema.features.pages.base_page import BasePage


class SignUpPage(BasePage):
    URL = 'https://jules.app/sign-up'

    def signup_button_selector(self):
        signup_button = (By.XPATH, "//a[normalize-space()='Sign up.']")
        return self.driver.find_element(*signup_button)

    def personal_button_selector(self):
        personal_button = (By.XPATH, "(//span[contains(text(),'PERSONAL')])[1]")
        return self.driver.find_element(*personal_button)

    def first_name_selector(self):
        first_name_field = (By.XPATH, "//input[@placeholder='Type your answer here...']")
        return self.driver.find_element(*first_name_field)

    def continue_button_selector(self):
        continue_button = (By.XPATH, "//span[normalize-space()='CONTINUE']")
        return self.driver.find_element(*continue_button)

    def last_name_selector(self):
        last_name_field = (By.XPATH, "//input[@placeholder='Type your answer here...']")
        return self.driver.find_element(*last_name_field)

    def email_selector(self):
        email_field = (By.XPATH, "//input[@placeholder='Type your answer here...']")
        return self.driver.find_element(*email_field)

    def invalid_email_error_selector(self):
        email_error = (By.TAG_NAME, "p")
        return self.driver.find_element(*email_error)

    def login_button_selector(self):
        login_button = (By.XPATH, "//span[normalize-space()='Log In.']")
        return self.driver.find_element(*login_button)


